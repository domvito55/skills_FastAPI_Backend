# -*- coding: utf-8 -*-
"""
Package Name: services
Description: This package contains service classes for the chat application.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55

This package includes the following service:
- IdeationService: Manages chat-based ideation sessions using AWS Bedrock and LangChain.
- ChatHistoryService: Manages chat history data storage and retrieval.
- MessageListService: Manages messages in a FILO (stack) style.


These services provide the core functionality for the chat application,
handling interactions with external APIs and processing chat messages.
"""

from .ideationChatServices import IdeationService, ChatHistoryService, MessageListService
from .pageBPServices import PageBPService

__all__ = ['IdeationService', 'ChatHistoryService', 'MessageListService',
           'PageBPService']
