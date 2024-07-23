# -*- coding: utf-8 -*-
"""
File Name: ideation.py
Description: This module provides the IdeationService class for managing
 chat-based ideation sessions.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.1
License: MIT License
Contact Information: mathteixeira55
"""

### imports ###
from time import time
from fastapi.encoders import jsonable_encoder
from httpx import AsyncClient, Response
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import boto3

from core.config import ideation
from core.config import aws
from models import Message


class IdeationService:
  """
    A service class for managing chat-based ideation sessions using AWS Bedrock and LangChain.

    This class handles the initialization of the chat model, manages chat history,
    and provides methods for running chat sessions and retrieving session history.

    Attributes:
        client (boto3.client): AWS Bedrock client.
        model (ChatBedrock): LangChain chat model for AWS Bedrock.
        prompt (ChatPromptTemplate): Template for structuring chat prompts.
        chain (Runnable): LangChain runnable chain for processing chat messages.
        asyncHttpClient (AsyncClient): Async HTTP client for database interactions.
        CHATHISTORY_DB_URL (str): URL for the chat history database.
    """

  def __init__(
      self,
      AWS_SERVICE_NAME: str = ideation.AWS_SERVICE_NAME,
      AWS_REGION: str = ideation.AWS_REGION,
      MODEL: str = ideation.MODEL,
      MAX_TOKENS: int = ideation.MAX_TOKENS,
      TEMPERATURE: int = ideation.TEMPERATURE,
      CHATHISTORY_DB_URL: str = ideation.CHATHISTORY_DB_URL,
      CHATHISTORY_COLLECTION_NAME: str = ideation.CHATHISTORY_COLLECTION_NAME,
      CHATHISTORY_SEARCH_FIELD: str = ideation.CHATHISTORY_SEARCH_FIELD,
      MESSAGE_LIST_URL: str = ideation.MESSAGE_LIST_URL):
    """
    Initialize the IdeationService with configuration parameters.

    Args:
        AWS_SERVICE_NAME (str): Name of the AWS service to use.
        AWS_REGION (str): AWS region for the service.
        MODEL (str): ID of the model to use.
        MAX_TOKENS (int): Maximum number of tokens for model output.
        TEMPERATURE (int): Temperature setting for model output.
        CHATHISTORY_DB_URL (str): URL for the chat history database.
        CHATHISTORY_COLLECTION_NAME (str): Name of the chat history collection.
        CHATHISTORY_SEARCH_FIELD (str): Field to search for chat history.
        MESSAGE_LIST_URL (str): URL for the message list operations.
    """
    self.client = boto3.client(
        service_name=AWS_SERVICE_NAME,
        region_name=AWS_REGION,
        aws_access_key_id=aws.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=aws.AWS_SECRET_ACCESS_KEY,
    )
    self.model = ChatBedrock(model_id=MODEL,
                             client=self.client,
                             model_kwargs={
                                 'max_tokens': MAX_TOKENS,
                                 'temperature': TEMPERATURE
                             })
    self.prompt = ChatPromptTemplate.from_messages([
        SystemMessage(
            content=
            'Answer to the best of your ability. Use Markdown for formating.'
            # """You should answer in {language}.
            # Your task is act as an advisor and moderator, and guide the user through the process of generating ideas for a new business or project.
            # You can ask questions, give suggestions, and provide feedback.
            # Do the process as if you were a human advisor, not a machine.
            # Do not be overwhelming or pushy, and do not provide too much information at once.
            # This should feel like a natural and enjoyable conversation between two people.
            # Ask questions to understand the user's needs and preferences, and provide suggestions based on the user's answers.
            # Ask one question at a time and use accessible language, so anyone trying to start a new business can understand.
            # Start asking general questions to understand the user's interests and goals, and then ask more specific questions to narrow down the ideas.
            # You should give professional advice taking into account the user's needs and preferences, the world and local market and trends, the user's skills and resources, macro and microeconomic factors, and other relevant aspects.
            # You can also provide feedback on the user's ideas and ask follow-up questions to help the user refine their ideas.
            # The goal is to help the user generate creative and innovative ideas for a new business or project.
            # You can also provide general advice on how to generate ideas and how to turn ideas into reality.
            # """
        ),
        MessagesPlaceholder(variable_name="messages"),
    ])

    self.chain = self.prompt | self.model
    # Initialize HTTP client for interacting with the chat history database
    # It must be closed when the service is done
    # It must be asynchroneous to avoid interlocking the main event loop
    # For example, the engoing chat POST request
    self.asyncHttpClient: AsyncClient = AsyncClient()
    self.CHATHISTORY_DB_URL = CHATHISTORY_DB_URL
    self.CHATHISTORY_COLLECTION_NAME = CHATHISTORY_COLLECTION_NAME
    self.CHATHISTORY_SEARCH_FIELD = CHATHISTORY_SEARCH_FIELD
    self.MESSAGE_LIST_URL = MESSAGE_LIST_URL

  async def getSessionHistory(
      self, fieldValue: str) -> tuple[ChatMessageHistory, str]:
    """
    Retrieve the chat history for a given session from the database.

    Args:
        fieldValue (str): The value of the field to search for.

    Returns:
        ChatMessageHistory: The chat history for the specified session.

    Raises:
        Exception: If there's an error retrieving the chat history.
    """
    try:
      # Retrieve chat history from database
      # before = time()
      response: Response = await self.asyncHttpClient.get(
          f"{self.CHATHISTORY_DB_URL}/{self.CHATHISTORY_COLLECTION_NAME}/{self.CHATHISTORY_SEARCH_FIELD}/{fieldValue}",
          timeout=10)
      # after = time()
      # print(f"Time to get chat history: {after - before}")

      # Check if response is successful
      response.raise_for_status()

      # Parse response (expected to be JSON with message and code keys)
      data: dict = response.json()
      result: dict = data["message"]

      chatHistory: ChatMessageHistory = ChatMessageHistory()
      if isinstance(result, dict) and "messages" in result:
        for msg in result["messages"]:
          if msg["type"] == "ai":
            chatHistory.add_message(AIMessage(content=msg["content"]))
          else:
            chatHistory.add_message(HumanMessage(content=msg["content"]))
      else:
        print(f"Unexpected response format: {data}")
        print(f"Returning empty chat history.")

      return chatHistory, result["_id"]
    except Exception as e:
      print(f"Error getting chat history: {str(e)}")
      print(f"Returning empty chat history.")
      # Return empty history on error
      return ChatMessageHistory()

  async def messageOperation(self, sessionID: str, operation: str,
                             newMessages: list[Message] | None) -> bool:
    """
    Push a new message to the chat history for a given session in the database.

    Args:
        sessionID (str): The ID of the chat session to update.
        newMessages (list[Message]): The new message to be added.

    Returns:
        ChatMessageHistory: The updated chat history for the specified session.

    Raises:
        Exception: If there's an error updating the chat history.
    """
    try:
      # Do the required operation (push or pop) on the chat history
      payload = jsonable_encoder(newMessages) if newMessages else None
      response: Response = await self.asyncHttpClient.post(
          f"{self.MESSAGE_LIST_URL}/{operation}/{self.CHATHISTORY_COLLECTION_NAME}/{sessionID}",
          json=payload,
          timeout=10)

      # Check if response is successful
      response.raise_for_status()

      return True
    except Exception as e:
      print(f"Error updating chat history: {str(e)}")
      return False

  async def runChat(self,
                    inputMessage: str,
                    language: str = "English",
                    fieldValue: str = "Test"):
    """
    Run a chat session with the given input message.

    Args:
        inputMessage (str): The user's input message.
        language (str, optional): The language to use for the response. Defaults to "English".
        fieldValue (str, optional): The value of the field that will identify the session. Defaults to "Test".

    Yields:
        str: Chunks of the AI's response.

    Raises:
        Exception: If there's an error during the chat process.
    """
    # Get chat history from database
    # print("Getting chat history...")
    # before = time()
    chatHistory: ChatMessageHistory
    chatId: str
    chatHistory, chatId = await self.getSessionHistory(fieldValue)
    # after = time()
    # print(f"Time to get chat history: {after - before}")

    # Add user new input to the chat history (in Memory)
    # print("Adding user input to chat history...")
    # before = time()
    chatHistory.add_message(HumanMessage(content=inputMessage))
    # after = time()
    # print(f"Time to add user input to chat history: {after - before}")

    # Input dict with all messages
    # print("Creating input dict...")
    # before = time()
    inputDict = {"messages": chatHistory.messages, "language": language}
    # after = time()
    # print(f"Time to create input dict: {after - before}")
    # print("Input Dict: \n", inputDict)

    # return the response, using plain text, in a streaming fashion
    full_response = ""
    # print("executing chain...")
    # before = time()
    async for chunk in self.chain.astream(inputDict):
      full_response += chunk.content
      yield chunk.content
      # print("Chunk (repr): ", repr(chunk.content))
    # after = time()
    # print("time to execute chain: ", after - before)
    # print(f"Generated chunk: {repr(full_response)}")
    messagesToPush = [
        Message(content=inputMessage, type="human"),
        Message(content=full_response, type="ai")
    ]
    # print("Pushing new content to chat history...")
    # before = time()
    newContentSaved: bool = await self.messageOperation(chatId, "push", messagesToPush)
    # after = time()
    # print(f"Time to push new content to chat history: {after - before}")
    if not newContentSaved:
      print("Failed to save new content to chat history.")

  async def close(self):
    """
    Close the async HTTP client.

    This method should be called when the IdeationService is no longer needed
    to ensure proper cleanup of resources.
    """
    await self.asyncHttpClient.aclose()
