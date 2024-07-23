# -*- coding: utf-8 -*-
"""
File Name: main.py
Description: This is the main entry point for the Skills Ladder API. It sets up
 the FastAPI  application, includes routers, and defines the base endpoints.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from schemas import ResponseSchema
from routers import chatHistoryRouter, ideationRouter, messageListRouter, pageBPRouter
from core.database import getNoSqlConn


@asynccontextmanager
async def lifespan(app: FastAPI):
  print("Starting up...")
  app.noSqlConn = getNoSqlConn()
  yield
  print("Shutting down...")
  app.noSqlConn.shutdownDbClient()


### Initialize FastAPI App ###
app = FastAPI(
    title="Skills Ladder API",
    version="1.0.0",
    lifespan=lifespan,
    description=
    "API for the Skills Ladder application, providing ideation and chat history functionalities."
)

### Include Routers ###
# Uncomment and modify these lines if you add authentication and user management in the future
# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# app.include_router(users.router, prefix="/api/users", tags=["Users"])

app.include_router(ideationRouter, prefix="/api/ideation", tags=["Ideation"])
app.include_router(chatHistoryRouter,
                   prefix="/api/chathistory",
                   tags=["Chat History"])
app.include_router(messageListRouter,
                   prefix="/api/messages",
                   tags=["Message List"])
app.include_router(pageBPRouter,
                   prefix="/api/pagebp",
                   tags=["1-Page Business Plan"])

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


### API Endpoints ###
@app.get("/check",
         tags=["Health Check"],
         summary="Health Check",
         response_model=ResponseSchema)
def health_check() -> ResponseSchema:
  """
    Health check endpoint for the Skills Ladder API.

    Returns:
        ResponseSchema: A dictionary containing a welcome message and a status code.
    """
  return ResponseSchema(message="Welcome to the Skills Ladder API!", code=200)


### Main ###
if __name__ == "__main__":
  import uvicorn

  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
