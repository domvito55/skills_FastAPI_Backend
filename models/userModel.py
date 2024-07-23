# -*- config: utf-8 -*-
"""
File Name: userModel.py
Description: This script defines the User model for representing and managing
 user data in the application.
Author: MathTeixeira
Date: July 6, 2024
Version: 4.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### imports ###
from pydantic import ConfigDict
from sqlmodel import Field, SQLModel, Column, VARCHAR
from passlib.context import CryptContext


class User(SQLModel, table=True):
    """
  User model for representing and managing user data in the application.

  Attributes:
    id (int): The unique identifier for the user.
    username (str): The username of the user.
    passwordHash (str): The hashed password of the user.
  """
    id: int | None = Field(None,
                           primary_key=True,
                           description="The unique identifier for the user")
    username: str = Field(
        ...,
        sa_column=Column("username", VARCHAR, unique=True, index=True),
        description="The username of the user")
    passwordHash: str = Field("",
                              description="The hashed password of the user")

    model_config = ConfigDict(from_attributes=True)

    def setPasswrod(self, password: str) -> None:
        """
    Set the password hash for the user.

    Args:
      password (str): The password to hash and store for the user.
    """
        passContext = CryptContext(schemes=["bcrypt"])
        self.passwordHash = passContext.hash(password)

    def verifyPassword(self, password: str) -> bool:
        """
    Verify the password for the user.

    Args:
      password (str): The password to verify against the stored hash.

    Returns:
      bool: True if the password matches the stored hash, False otherwise.
    """
        passContext = CryptContext(schemes=["bcrypt"])
        return passContext.verify(password, self.passwordHash)
