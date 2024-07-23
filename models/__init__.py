# -*- coding: utf-8 -*-
"""
Package Name: models
Description: This package contains the data models for the chat application,
 including User, ChatHistory, and Message models.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55

This package defines the core data structures used in the chat application.
It includes models for representing users, chat histories, and individual messages.
These models are used throughout the application for data handling and storage.
"""

from .userModel import User
from .chatHistoryModel import ChatHistory
from .messageModel import Message

__all__ = ['User', 'ChatHistory', 'Message']
