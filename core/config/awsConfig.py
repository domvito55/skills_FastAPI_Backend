# -*- coding: utf-8 -*-
"""
File Name: awsConfig.py
Description: This module handles the configuration of AWS connection using
 environment variables.
Author: MathTeixeira
Date: July 9, 2024
Version: 1.1.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from dotenv import load_dotenv
import os


class AWSConfig:
  """
  Config class to load environment variables and provide AWS configuration values.
  
  This class implements a singleton pattern with lazy loading to ensure
  only one instance is created and only when it's first needed.

  Attributes:
    AWS_ACCESS_KEY_ID (str): The AWS access key ID.
    AWS_SECRET_ACCESS_KEY (str): The AWS secret access key.

  Raises:
    ValueError: If required environment variables are not set.
  """

  instance: 'AWSConfig | None' = None

  def __init__(self) -> None:
    """
    Initialize the AWSConfig instance.

    Loads environment variables and sets AWS credentials.

    Raises:
      ValueError: If required environment variables are not set.
    """
    load_dotenv()
    self.AWS_ACCESS_KEY_ID: str = self.getEnv('AWS_ACCESS_KEY_ID')
    self.AWS_SECRET_ACCESS_KEY: str = self.getEnv('AWS_SECRET_ACCESS_KEY')

  @classmethod
  def getInstance(cls) -> 'AWSConfig':
    """
    Get the singleton instance of AWSConfig.

    Returns:
      AWSConfig: The singleton instance of AWSConfig.

    This method ensures that only one instance of AWSConfig is created.
    """
    if cls.instance is None:
      cls.instance = cls()
    return cls.instance

  def getEnv(self, key: str) -> str:
    """
    Get an environment variable or raise an exception if it's not set.

    Args:
      key (str): The name of the environment variable.

    Returns:
      str: The value of the environment variable.

    Raises:
      ValueError: If the environment variable is not set.
    """
    value = os.getenv(key)
    if value is None:
      raise ValueError(f"Environment variable '{key}' is not set")
    return value


# Global instance of AWSConfig
# This will not create the instance until it's first accessed
aws = AWSConfig.getInstance()
