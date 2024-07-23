# -*- coding: utf-8 -*-
"""
Package Name: routers
Description: This package contains the API routers for the SkillsLadder application.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55

This package includes routers for different functionalities of the chat application:
- chathistoryRouter: Handles endpoints related to chat history operations.
- ideationRouter: Manages endpoints for the ideation chatbot functionality.
- messageListRouter: Manages endpoints for managing messages in a FILO (stack) style.

These routers are used to organize and structure the API endpoints of the application.
"""

from .ideationChatRouters import chatHistoryRouter, ideationRouter, messageListRouter
from .pageBPRouter import pageBPRouter

__all__ = ['chatHistoryRouter', 'ideationRouter', 'messageListRouter', 'pageBPRouter']
