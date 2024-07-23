# -*- coding: utf-8 -*-
"""
File Name: chatRequestSchema.py
Description: This module defines the schema for chat requests in the API.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from pydantic import BaseModel, Field, ConfigDict


class ChatRequestSchema(BaseModel):
  """
  ChatRequestSchema for structuring API requests.

  This schema defines the structure of chat requests sent to the API.
  It ensures that incoming requests contain the necessary message field.

  Attributes:
    message (str): The message to be sent in the chat.
  """
  message: str = Field(..., description="The message to be sent in the chat")

  model_config = ConfigDict(json_schema_extra={
      "example": {
          "message": "What is my name?"
      }
  })
