# -*- coding: utf-8 -*-
"""
File Name: messageListRouter.py
Description: This module defines the API routes for managing messages in a FILO (stack) style.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from fastapi import APIRouter, HTTPException, status

from services import MessageListService
from models import Message
from schemas import ResponseSchema
from utils import collectionPath, sessionPath

messageListRouter = APIRouter()


@messageListRouter.post("/push/{collectionName}/{sessionId}",
                        summary="Push new messages to chat session",
                        status_code=status.HTTP_201_CREATED,
                        response_model=ResponseSchema)
async def pushMessages(*,
                      collectionName: str = collectionPath,
                      sessionId: str = sessionPath,
                      newMessage: list[Message]) -> ResponseSchema:
  """
  Push a new message to the end of the messages list in a chat session.

  This endpoint accepts a Message object and adds it to the messages list of a specified chat session.

  Args:
      collectionName (str): The name of the collection to update.
      sessionId (str): The ID of the chat session to update.
      newMessage (list[Message]): The message to be added.

  Returns:
      ResponseSchema: A response indicating success and a status code.

  Raises:
      HTTPException: If there's an error pushing the message.
  """
  try:
    success = await MessageListService.pushMessages(collectionName, sessionId,
                                                   newMessage)
    if not success:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail="Failed to push messages")
    return ResponseSchema(message="Messages pushed successfully",
                          code=status.HTTP_201_CREATED)
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=str(e))


@messageListRouter.delete(
    "/pop/{collectionName}/{sessionId}",
    summary="Pop last message from chat session",
    response_model=ResponseSchema)
async def popMessage(collectionName: str, sessionId: str) -> ResponseSchema:
  """
  Pop the last message from the messages list in a chat session.

  This endpoint removes the last message from the messages list of a specified chat session.

  Args:
      collectionName (str): The name of the collection to update.
      sessionId (str): The ID of the chat session to update.

  Returns:
      ResponseSchema: A response containing the removed message and a status code.

  Raises:
      HTTPException: If there's an error popping the message.
  """
  try:
    removedMessage = await MessageListService.popMessage(
        collectionName, sessionId)
    if not removedMessage:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail="Failed to pop message")
    return ResponseSchema(message=removedMessage, code=status.HTTP_200_OK)
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=str(e))
