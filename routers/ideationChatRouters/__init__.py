# -*- coding: utf-8 -*-
"""
Package Name: ideationChatRouters
Description: This package contains the API routers for the chat application.
Author: MathTeixeira
Date: July 19, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55

This package includes routers for different functionalities of the chat application:
- chathistoryRouter: Handles endpoints related to chat history operations.
- ideationRouter: Manages endpoints for the ideation chatbot functionality.
- messageListRouter: Manages endpoints for managing messages in a FILO (stack) style.

These routers are used to organize and structure the API endpoints of the application.
"""

from .chatHistoryRouter import chatHistoryRouter
from .ideationRouter import ideationRouter
from .messageListRouter import messageListRouter

__all__ = ['chatHistoryRouter', 'ideationRouter', 'messageListRouter']
