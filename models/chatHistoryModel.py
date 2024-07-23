# -*- coding: utf-8 -*-
"""
File Name: chatHistoryModel.py
Description: This module defines the ChatHistory model for representing chat
 sessions.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
import uuid
from pydantic import BaseModel, ConfigDict, Field
from .messageModel import Message


class ChatHistory(BaseModel):
  """
  Represents a chat history session.

  This model stores information about a chat session, including its unique
   identifier, session name, and a list of messages exchanged during the session.

  Attributes:
    id (str): The unique identifier for the chat history. Defaults to a UUID.
    sessionName (str): The name of the chat session.
    messages (list[Message]): A list of messages in the chat history.

  Config:
    The model uses Pydantic's ConfigDict for additional configuration.
  """

  id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
  sessionName: str = Field(...)
  messages: list[Message] = Field(default_factory=list)

  model_config = ConfigDict(
      from_attributes=True,
      json_schema_extra={
        "example": {
            "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
            "sessionName": "Test",
            "messages": [
              {
                "type": "human",
                "content": "Hello, how are you?"
              },
              {
                "type": "ai",
                "content": "I'm doing well, thank you for asking!"
              }
            ]
          }
        }
      )
