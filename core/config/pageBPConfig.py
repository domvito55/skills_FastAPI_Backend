# -*- coding: utf-8 -*-
"""
File Name: pgBPConfig.py
Description: This module handles the configuration related to the 1-page BP.
Author: MathTeixeira
Date: July 9, 2024
Version: 1.1.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
import os


class PageBPConfig:
  """
  Config class to load environment variables and provide configuration values for the 1-page BP.

  This class implements a singleton pattern with lazy loading to ensure
  only one instance is created and only when it's first needed.

  Attributes:
    AWS_SERVICE_NAME (str): The name of the AWS service to use.
    AWS_REGION (str): The AWS region to use.
    MAX_TOKENS (int): Maximum tokens to generate for the output.
    TEMPERATURE (float): Temperature parameter for sampling creativity.
    MODEL (str): The model to use for the chatbot.
  """

  instance: 'PageBPConfig | None' = None

  def __init__(self, langchainTrack: bool = True) -> None:
    """
    Initialize the PageBPConfig instance.

    Args:
      langchainTrack (bool): Whether to enable Langchain tracking. Defaults to True.
    """
    self.AWS_SERVICE_NAME: str = 'bedrock-runtime'
    self.AWS_REGION: str = 'us-east-1'
    self.MAX_TOKENS: int = 5000
    self.TEMPERATURE: float = 0.7
    self.MODEL: str = 'anthropic.claude-3-haiku-20240307-v1:0'

    if langchainTrack:
      os.environ["LANGCHAIN_PROJECT"] = "skillsLangSmith"

  @classmethod
  def getInstance(cls, langchainTrack: bool = True) -> 'PageBPConfig':
    """
    Get the singleton instance of PageBPConfig.

    Args:
      langchainTrack (bool): Whether to enable Langchain tracking. Defaults to True.

    Returns:
      PageBPConfig: The singleton instance of PageBPConfig.

    This method ensures that only one instance of PageBPConfig is created.
    """
    if cls.instance is None:
      cls.instance = cls(langchainTrack)
    return cls.instance


# Global instance of PageBPConfig
# This will create the instance when the module is imported
pageBP: PageBPConfig = PageBPConfig.getInstance()
