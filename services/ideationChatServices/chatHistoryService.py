# -*- coding: utf-8 -*-
"""
File Name: chatHistoryService.py
Description: This module contains the business logic for managing chat history.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.2.0
License: MIT License
Contact Information: mathteixeira55
"""

from fastapi.encoders import jsonable_encoder
import logging
from core.database import getNoSqlConn
from models import ChatHistory


class ChatHistoryService:
  """
  A service class for managing chat history business logic.
  """

  @staticmethod
  async def createChatHistory(collectionName: str,
                              chatHistory: ChatHistory) -> ChatHistory:
    """
    Create a new chat history document.

    Args:
      collectionName (str): The name of the collection to insert the document into.
      chatHistory (ChatHistory): The chat history data to be inserted.

    Returns:
      ChatHistory: The created chat history document.
    """
    try:
      chatHistory = jsonable_encoder(chatHistory)
      createdChatHistory = getNoSqlConn().insertDocument(
          collectionName, chatHistory)
      createdChatHistory = ChatHistory.model_validate(createdChatHistory)
      return createdChatHistory
    except Exception as e:
      logging.error(f"Error creating chat history: {e}")
      return None

  @staticmethod
  async def getChatHistoryByField(collectionName: str, field: str,
                                  value: str) -> ChatHistory:
    """
    Retrieve a chat history document by a specified field and its value.

    Args:
      collectionName (str): The name of the collection to search in.
      field (str): The field to search by.
      value (str): The value of the field to search for.

    Returns:
      ChatHistory: The retrieved chat history document or None if not found.
    """
    try:
      chatHistory = getNoSqlConn().findDocumentByField(collectionName, field,
                                                       value)
      chatHistory = ChatHistory.model_validate(chatHistory)
      return chatHistory
    except Exception as e:
      logging.error(f"Error retrieving chat history by {field}: {e}")
      return None

  @staticmethod
  async def updateChatHistory(collectionName: str, field: str, value: str,
                              chatHistory: ChatHistory) -> bool:
    """
    Update an existing chat history document by a specified field and its value.

    Args:
      collectionName (str): The name of the collection to update the document in.
      field (str): The field to search by.
      value (str): The value of the field to search for.
      chatHistory (ChatHistory): The updated chat history data.

    Returns:
      bool: True if the chat history was successfully updated, False otherwise.
    """
    try:
      chatHistory = jsonable_encoder(chatHistory)
      updateResult = getNoSqlConn().updateDocument(collectionName,
                                                   {field: value}, chatHistory)
      return updateResult is not None
    except Exception as e:
      logging.error(f"Error updating chat history by {field}: {e}")
      return False

  @staticmethod
  async def deleteChatHistory(collectionName: str, field: str,
                              value: str) -> bool:
    """
    Delete a chat history document by a specified field and its value.

    Args:
      collectionName (str): The name of the collection to delete the document from.
      field (str): The field to search by.
      value (str): The value of the field to search for.

    Returns:
      bool: True if the document was deleted, False otherwise.
    """
    try:
      deleteResult = getNoSqlConn().deleteDocument(collectionName,
                                                   {field: value})
      return deleteResult
    except Exception as e:
      logging.error(f"Error deleting chat history by {field}: {e}")
      return False
