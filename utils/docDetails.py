# -*- coding: utf-8 -*-
"""
File Name: docDetails.py
Description: This module contains query and path parameters for API documentation.
Author: MathTeixeira
Date: July 12, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from fastapi import Query, Path

### Query Parameters ###
# Query is used to define query parameters for the API endpoints.
# These definitions also provide Swagger documentation for the query parameters.
# sizeQuery: str | None = Query(
#     None,
#     description="Filter cars by size (s, m, l)",
#     openapi_examples={"small": {
#         "summary": "Small car",
#         "value": "s"
#     }})

### Path Parameters ###
# Path is used to define path parameters for the API endpoints.
collectionPath: str = Path(
    ...,
    description="Collection name for the database",
    openapi_examples={
        "Chat History": {
            "summary": "Chat History Collection",
            "value": "chatHistories"
        }
    })

fieldPath: str = Path(
    ...,
    description="Field to be searched in the database",
    openapi_examples={
        "sessionName": {
            "summary": "The name of the session",
            "value": "sessionName"
        }
    })

valuePath: str = Path(
    ...,
    description="Value to be searched in the database",
    openapi_examples={
        "Test": {
            "summary": "The name of the session",
            "value": "Test"
        }
    })

sessionPath: str = Path(
    ...,
    description="Session ID for the chat history",
    openapi_examples={
        "Test": {
            "summary": "The ID of the session",
            "value": "be46af78-63da-42d8-9145-ea99419689c4"
        }
    })
