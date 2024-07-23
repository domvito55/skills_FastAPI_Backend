# -*- coding: utf-8 -*-
"""
File Name: userSchema.py
Description: This script defines the UserSchema for data validation and
 serialization of user data in the application. The schema includes fields for
 the username and hashed password of the user.
Author: MathTeixeira
Date: July 6, 2024
Version: 4.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
  """
  UserSchema model for data validation and serialization.

  Attributes:
    id (int, optional): The unique identifier for the user.
    username (str): The username of the user.
    passwordHash (str): The hashed password of the user.
  """
  username: str = Field(...,
                        description="The username of the user",
                        json_schema_extra={"example": "johndoe"})
  password: str = Field("",
                        description="The hashed password of the user",
                        json_schema_extra={"example": "password123"})
