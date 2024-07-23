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
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from schemas import PageBPRequestSchema
from services import PageBPService

pageBPRouter = APIRouter()

# --- POST / ---
@pageBPRouter.post('/', summary='Generate Business Plan markdown')
def businessPlan(pageBPRequest: PageBPRequestSchema):
  """
  Endpoint to generate a business plan markdown.

  This function handles POST requests to generate a business plan markdown based on the user's input.

  Args:
    pageBPRequest (PageBPRequestSchema): The business plan request containing the user's input.

  Returns:
    StreamingResponse: A streaming response containing the business plan markdown.

  Raises:
    HTTPException: If there's an error during content generation
  """

  pageBPService = PageBPService()

  businessInfo = pageBPRequest.businessInfo
  # print(f"businessInfo: {businessInfo}")

  if not businessInfo:
    raise HTTPException(status_code=400,
                        detail="Missing 'businessInfo' in request data")

  async def content_generator():
    """
    Generator function to stream the chatbot's response content.

    Yields:
      str: Chunks of the AI's response.

    Raises:
      Exception: If there's an error during content generation.
    """
    try:
      async for content in pageBPService.businessPlanQuery(businessInfo):
        yield f"{content}"
    except Exception as e:
      print(f"Error in content generation: {str(e)}")
      print(f"Traceback: {traceback.format_exc()}")
      yield f"Error: {str(e)}\n"

  return StreamingResponse(content_generator(), media_type="text/plain")
