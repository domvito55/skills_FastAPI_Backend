# -*- coding: utf-8 -*-
"""
Package Name: schemas
Description: This package contains the Pydantic schemas for data validation and
 serialization in the chat application.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55

This package includes the following schemas:
- ResponseSchema: Used for structuring API responses.
- UserSchema: Defines the structure for user data.
- UserProtectedSchema: A version of UserSchema with protected fields.
- ChatRequestSchema: Structures incoming chat requests.

These schemas are used throughout the application to ensure data consistency
and to provide clear interfaces for API requests and responses.
"""

from .responseSchema import ResponseSchema
from .userSchema import UserSchema
from .userProtectedSchema import UserProtectedSchema
from .chatRequestSchema import ChatRequestSchema
from .pageBPRequestSchema import PageBPRequestSchema

__all__ = [
    'ResponseSchema', 'UserSchema', 'UserProtectedSchema', 'ChatRequestSchema',
    'PageBPRequestSchema']
