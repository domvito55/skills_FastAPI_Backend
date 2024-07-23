# # -*- config: utf-8 -*-
# """
# File Name: users.py
# Description: This script defines the routers for managing users in the car
#  sharing service.
# Author: MathTeixeira
# Date: July 6, 2024
# Version: 4.0.0
# License: MIT License
# Contact Information: mathteixeira55
# """

# ### Imports ###
# from fastapi import APIRouter, Depends
# from sqlmodel import Session
# from models import User
# from schemas import UserSchema, UserProtectedSchema, ResponseSchema
# from core.database.sqlDatabase import sqlDb

# router = APIRouter()

# ### CRUD Operations for Users ###
# # Create
# @router.post("/signup",
#              summary="Register new user",
#              response_model=ResponseSchema)
# def signup(
#     user: UserSchema, session: Session = Depends(sqlDb.getSession)
# ) -> ResponseSchema:
#   """
#   Register a new user in the database.

#   Returns:
#     str: A message indicating that the user was successfully registered.
#   """
#   userToAdd = User(username=user.username)
#   userToAdd.setPasswrod(user.password)
#   session.add(userToAdd)
#   session.commit()
#   session.refresh(userToAdd)
#   print("-" * 50)
#   print("userToAdd:", userToAdd)
#   print("type userToAdd:", type(userToAdd))
#   AddedUser = UserProtectedSchema.model_validate(userToAdd)

#   return ResponseSchema(message=AddedUser, code=201)
