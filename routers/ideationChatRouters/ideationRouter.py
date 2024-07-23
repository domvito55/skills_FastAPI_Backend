# -*- coding: utf-8 -*-
"""
File Name: ideationRouter.py
Description: This module defines the FastAPI router for the ideation chatbot endpoint.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

import traceback
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from schemas import ChatRequestSchema
from services import IdeationService

ideationRouter = APIRouter()


@ideationRouter.post("/", summary="Run Ideation Chatbot")
async def runIdeationChatbot(chatRequest: ChatRequestSchema):
  """
  Endpoint to run the ideation chatbot.

  This function handles POST requests to the ideation chatbot. It takes a chat request,
  processes it through the IdeationService, and returns a streaming response of the chatbot's output.

  Args:
    chatRequest (ChatRequestSchema): The chat request containing the user's message.

  Returns:
    StreamingResponse: A streaming response containing the chatbot's generated content.

  Raises:
    Exception: Any exception that occurs during content generation is caught and its message is yielded.
  """
  message = chatRequest.message
  ideationService = IdeationService()

  async def content_generator():
    """
    Generator function to stream the chatbot's response content.

    Yields:
      str: Chunks of the AI's response.

    Raises:
      Exception: If there's an error during content generation.
    """
    try:
      async for content in ideationService.runChat(message):
        yield f"{content}"
      await ideationService.close()
    except Exception as e:
      print(f"Error in content generation: {str(e)}")
      print(f"Traceback: {traceback.format_exc()}")
      yield f"Error: {str(e)}\n"
      await ideationService.close()

  return StreamingResponse(content_generator(), media_type="text/plain")
