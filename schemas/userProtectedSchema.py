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
from pydantic import BaseModel, ConfigDict, Field


class UserProtectedSchema(BaseModel):
  """
  UserSchema model for data validation and serialization.

  Attributes:
    username (str): The username of the user.
  """
  id: int | None = Field(None,
                         description="The unique identifier for the user",
                         json_schema_extra={"example": 5})
  username: str = Field(...,
                        description="The username of the user",
                        json_schema_extra={"example": "johndoe"})

  model_config = ConfigDict(from_attributes=True)
