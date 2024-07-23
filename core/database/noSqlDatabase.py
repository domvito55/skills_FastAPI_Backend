# -*- coding: utf-8 -*-
"""
File Name: noSqlDatabase.py
Description: This module provides a class for interacting with a NoSQL database.
Author: MathTeixeira
Date: July 10, 2024
Version: 1.2.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from pymongo import MongoClient, errors
from pymongo.database import Database
from core.config import noSql


class NoSqlConnection:
  """
  A class to handle connections and operations with a NoSQL database.

  This class provides methods to connect to a NoSql database and perform basic
  operations.

  Attributes:
    dbUrl (str): The URL for the NoSql connection.
    dbName (str): The name of the database to connect to.
    NoSqlClient (MongoClient): The NoSql client instance.
    database (Database): The NoSql database instance.
  """

  _instance: 'NoSqlConnection | None' = None

  def __init__(self, dbUrl: str = noSql.URL, dbName: str = noSql.NAME):
    """
    Initialize the NoSqlConnection instance.

    Args:
      dbUrl (str): The URL for the NoSql connection. Defaults to the URL from noSqlConfig.
      dbName (str): The name of the database to connect to. Defaults to the NAME from noSqlConfig.
    """
    self.dbUrl: str = dbUrl
    self.dbName: str = dbName

    try:
      self.NoSqlClient: MongoClient = MongoClient(dbUrl)
      self.database: Database = self.NoSqlClient[dbName]
      print("Connected to the NoSql database!")
    except errors.ConnectionError as e:
      print(f"Connection error: {e}")

  @classmethod
  def getInstance(cls) -> 'NoSqlConnection':
    """
    Get the singleton instance of NoSqlDatabase.

    Returns:
      NoSqlDatabase: The singleton instance of NoSqlDatabase.
    """
    if cls._instance is None:
      cls._instance = cls()
    return cls._instance

  def shutdownDbClient(self) -> None:
    """
    Close the NoSql client connection.
    """
    self.NoSqlClient.close()
    print("NoSql connection closed.")

  def insertDocument(self, collection_name: str, document: dict) -> dict:
    """
    Insert a document into a specified collection.

    Args:
      collection_name (str): The name of the collection to insert the document into.
      document (dict): The document to be inserted.

    Returns:
      dict: The inserted document with its ID.
    """
    try:
      newDocument = self.database[collection_name].insert_one(document)
      insertedDocument = self.database[collection_name].find_one(
          {"_id": newDocument.inserted_id})
      return insertedDocument
    except errors.PyMongoError as e:
      print(f"Error inserting document: {e}")
      return None

  def findDocumentByField(self, collection_name: str, field: str,
                          value: str) -> dict:
    """
    Find a document in a specified collection by a field and its value.

    Args:
      collection_name (str): The name of the collection to search in.
      field (str): The field to search by.
      value (str): The value of the field to search for.

    Returns:
      dict: The found document or None if no document is found.
    """
    try:
      document = self.database[collection_name].find_one({field: value})
      return document
    except errors.PyMongoError as e:
      print(f"Error finding document: {e}")
      return None

# Alias for NoSqlConnection.getInstance
# This alias allows for easier access to the NoSqlDatabase singleton instance.
getNoSqlConn = NoSqlConnection.getInstance