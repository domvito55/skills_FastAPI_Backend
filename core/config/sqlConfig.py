# -*- coding: utf-8 -*-
"""
File Name: sqlConfig.py
Description: This module handles the configuration of the SQL database connection.
Author: MathTeixeira
Date: July 9, 2024
Version: 1.1.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from dotenv import load_dotenv
import os


class SqlConfig:
  """
  Config class to load environment variables and provide configuration values for SQL database connection.

  This class implements a singleton pattern with lazy loading to ensure
  only one instance is created and only when it's first needed.

  Attributes:
    USERNAME (str): The username for SQL database connection.
    PASSWORD (str): The password for SQL database connection.
    HOST (str): The host address of the SQL database.
    PORT (str): The port number for the SQL database connection.
    NAME (str): The name of the SQL database.

  Raises:
    ValueError: If required environment variables are not set.
  """

  instance: 'SqlConfig | None' = None

  def __init__(self) -> None:
    """
    Initialize the SqlConfig instance.

    Loads environment variables and sets SQL database connection details.

    Raises:
      ValueError: If required environment variables are not set.
    """
    load_dotenv()
    self.USERNAME: str = self.getEnv("SQL_USERNAME")
    self.PASSWORD: str = self.getEnv("SQL_PASSWORD")
    self.HOST: str = self.getEnv("SQL_HOST")
    self.PORT: str = self.getEnv("SQL_PORT")
    self.NAME: str = self.getEnv("SQL_NAME")

  @classmethod
  def getInstance(cls) -> 'SqlConfig':
    """
    Get the singleton instance of SqlConfig.

    Returns:
      SqlConfig: The singleton instance of SqlConfig.

    This method ensures that only one instance of SqlConfig is created.
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


# Global instance of SqlConfig
# This will create the instance when the module is imported
sql = SqlConfig.getInstance()
