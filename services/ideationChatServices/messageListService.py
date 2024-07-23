# -*- coding: utf8 -*-
"""
File Name: messageListService.py
Description: This module contains the business logic for managing messages in a FILO (stack) style.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from fastapi.encoders import jsonable_encoder
import logging
from core.database import getNoSqlConn
from models import Message


class MessageListService:
  """
  A service class for managing messages in a chat session.
  """

  @staticmethod
  async def pushMessages(collectionName: str, sessionId: str, newMessages: list[Message]) -> bool:
    """
    Push a list of new messages to the end of the messages list in a chat session.

    Args:
      collectionName (str): The name of the collection to update.
      sessionId (str): The ID of the chat session to update.
      newMessages (list[Message]): The list of messages to be added.

    Returns:
      bool: True if the messages were successfully pushed, False otherwise.
    """
    try:
      messages = jsonable_encoder(newMessages)
      updateResult = getNoSqlConn().database[collectionName].update_one(
          {"_id": sessionId},
          {"$push": {"messages": {"$each": messages}}}
      )
      return updateResult.modified_count > 0
    except Exception as e:
      logging.error(f"Error pushing messages: {e}")
      return False
    
  @staticmethod
  async def popMessage(collectionName: str, sessionId: str) -> Message:
    """
    Pop the last message from the messages list in a chat session.

    Args:
      collectionName (str): The name of the collection to update.
      sessionId (str): The ID of the chat session to update.

    Returns:
      Message: The removed message or None if no message was removed.
    """
    try:
      # Retrieve the chat session to get the last message
      chatSession = getNoSqlConn().database[collectionName].find_one(
          {"_id": sessionId})
      if not chatSession or not chatSession["messages"]:
        return None

      # Get the last message
      lastMessage = chatSession["messages"][-1]

      # Remove the last message
      updateResult = getNoSqlConn().database[collectionName].update_one(
          {"_id": sessionId}, {"$pop": {
              "messages": 1
          }})
      if updateResult.modified_count == 0:
        return None

      return Message.model_validate(lastMessage)
    except Exception as e:
      logging.error(f"Error popping message: {e}")
      return None
