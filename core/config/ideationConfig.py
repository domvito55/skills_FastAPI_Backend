# -*- coding: utf-8 -*-
"""
File Name: ideationConfig.py
Description: This module handles the configuration of the ideation chatbot.
Author: MathTeixeira
Date: July 9, 2024
Version: 1.1.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
import os


class IdeationConfig:
  """
  Config class to load environment variables and provide configuration values for the ideation chatbot.

  This class implements a singleton pattern with lazy loading to ensure
  only one instance is created and only when it's first needed.

  Attributes:
    AWS_SERVICE_NAME (str): The name of the AWS service to use.
    AWS_REGION (str): The AWS region to use.
    MAX_TOKENS (int): Maximum tokens to generate for the output.
    TEMPERATURE (float): Temperature parameter for sampling creativity.
    TRIM_SIZE (int): The maximum number of tokens to keep in the chat history.
    MODEL (str): The model to use for the chatbot.
    CHATHISTORY_DB_URL (str): URL for the chat history database.
  """

  instance: 'IdeationConfig | None' = None

  def __init__(self, langchainTrack: bool = True) -> None:
    """
    Initialize the IdeationConfig instance.

    Args:
      langchainTrack (bool): Whether to enable Langchain tracking. Defaults to True.
    """
    self.AWS_SERVICE_NAME: str = 'bedrock-runtime'
    self.AWS_REGION: str = 'us-east-1'
    self.MAX_TOKENS: int = 500
    self.TEMPERATURE: float = 0.7
    self.TRIM_SIZE: int = 500
    self.MODEL: str = 'anthropic.claude-3-haiku-20240307-v1:0'
    self.CHATHISTORY_DB_URL: str = 'http://localhost:8000/api/chathistory'
    self.CHATHISTORY_COLLECTION_NAME: str = 'chatHistories'
    self.CHATHISTORY_SEARCH_FIELD: str = 'sessionName'
    self.MESSAGE_LIST_URL: str = 'http://localhost:8000/api/messages'

    if langchainTrack:
      os.environ["LANGCHAIN_PROJECT"] = "skillsLangSmith"

  @classmethod
  def getInstance(cls, langchainTrack: bool = True) -> 'IdeationConfig':
    """
    Get the singleton instance of IdeationConfig.

    Args:
      langchainTrack (bool): Whether to enable Langchain tracking. Defaults to True.

    Returns:
      IdeationConfig: The singleton instance of IdeationConfig.

    This method ensures that only one instance of IdeationConfig is created.
    """
    if cls.instance is None:
      cls.instance = cls(langchainTrack)
    return cls.instance


# Global instance of IdeationConfig
# This will create the instance when the module is imported
ideation = IdeationConfig.getInstance()
