# -*- coding: utf-8 -*-
"""
File Name: chatHistoryRouter.py
Description: This module defines the API routes for managing chat history.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from fastapi import APIRouter, HTTPException, status

from services import ChatHistoryService
from models import ChatHistory
from schemas import ResponseSchema
from utils import collectionPath, fieldPath, valuePath

chatHistoryRouter = APIRouter()


# Create
@chatHistoryRouter.post("/{collectionName}",
                        summary="Create new chat history",
                        status_code=status.HTTP_201_CREATED,
                        response_model=ResponseSchema)
async def createChatHistory(*,
                            collectionName: str = collectionPath,
                            chatHistory: ChatHistory):
  """
  Create a new chat history entry.

  This endpoint accepts a ChatHistory object and stores it in the database.

  Args:
      collectionName (str): The name of the collection to insert the document into.
      chatHistory (ChatHistory): The chat history to be created.

  Returns:
      ResponseSchema: A response containing the created chat history and a status code.

  Raises:
      HTTPException: If there's an error creating the chat history.
  """
  try:
    createdChatHistory = await ChatHistoryService.createChatHistory(
        collectionName, chatHistory)
    if not createdChatHistory:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail="Failed to create chat history")
    return ResponseSchema(message=createdChatHistory,
                          code=status.HTTP_201_CREATED)
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=str(e))


# Retrieve
@chatHistoryRouter.get("/{collectionName}/{field}/{value}",
                       summary="Get History",
                       response_model=ResponseSchema)
async def getChatHistoryByField(collectionName: str = collectionPath,
                                field: str = fieldPath,
                                value: str = valuePath):
  """
  Retrieve a chat history session by a specified field and its value.

  Args:
      collectionName (str): The name of the collection to search in.
      field (str): The field to search by.
      value (str): The value of the field to search for.

  Returns:
      ResponseSchema: A response containing the chat history and a status code.

  Raises:
      HTTPException: If there's an error retrieving the chat history.
  """
  try:
    chatHistory = await ChatHistoryService.getChatHistoryByField(
        collectionName, field, value)
    if chatHistory:
      return ResponseSchema(message=chatHistory, code=status.HTTP_200_OK)
    else:
      return ResponseSchema(message="Chat history not found",
                            code=status.HTTP_404_NOT_FOUND)
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=str(e))


# Update
@chatHistoryRouter.put("/{collectionName}/{field}/{value}",
                       summary="Update History",
                       response_model=ResponseSchema)
async def updateChatHistory(collectionName: str, field: str, value: str,
                            chatHistory: ChatHistory):
  """
  Update an existing chat history session.

  Args:
      collectionName (str): The name of the collection to update the document in.
      field (str): The field to search by.
      value (str): The value of the field to search for.
      chatHistory (ChatHistory): The updated chat history data.

  Returns:
      ResponseSchema: A response containing a success message and a status code.

  Raises:
      HTTPException: If there's an error updating the chat history.
  """
  try:
    updateResult = await ChatHistoryService.updateChatHistory(
        collectionName, field, value, chatHistory)
    if updateResult:
      return ResponseSchema(message="Chat history updated successfully",
                            code=status.HTTP_200_OK)
    else:
      return ResponseSchema(message="Chat history not found",
                            code=status.HTTP_404_NOT_FOUND)
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=str(e))


# Delete
@chatHistoryRouter.delete("/{collectionName}/{field}/{value}",
                          summary="Delete History",
                          response_model=ResponseSchema)
async def deleteChatHistory(collectionName: str, field: str, value: str):
  """
  Delete a chat history session by a specified field and its value.

  Args:
      collectionName (str): The name of the collection to delete the document from.
      field (str): The field to search by.
      value (str): The value of the field to search for.

  Returns:
      ResponseSchema: A response containing a confirmation message and a status code.

  Raises:
      HTTPException: If there's an error deleting the chat history.
  """
  try:
    deleteResult = await ChatHistoryService.deleteChatHistory(
        collectionName, field, value)
    if deleteResult:
      return ResponseSchema(message="Chat history deleted successfully",
                            code=status.HTTP_200_OK)
    else:
      return ResponseSchema(message="Chat history not found",
                            code=status.HTTP_404_NOT_FOUND)
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=str(e))
