# -*- coding: utf-8 -*-
"""
File Name: messageModel.py
Description: This module defines the Message model for representing individual
 chat messages.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from pydantic import BaseModel, Field, ConfigDict


class Message(BaseModel):
  """
  Represents an individual message in a chat.

  This model stores information about a single message, including its type
  (e.g., "human" or "ai") and its content.

  Attributes:
    type (str): The type of the message, typically "human" or "ai".
    content (str): The actual content of the message.

  Config:
    The model uses Pydantic's ConfigDict for additional configuration.
  """

  type: str = Field(
      ..., description="The type of the message (e.g., 'human' or 'ai')")
  content: str = Field(..., description="The content of the message")

  model_config = ConfigDict(from_attributes=True,
                            json_schema_extra={
                                "example": {
                                    "type": "human",
                                    "content": "Hello, how are you?"
                                }
                            })
