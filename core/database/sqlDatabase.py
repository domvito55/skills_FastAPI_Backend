# -*- coding: utf-8 -*-
"""
File Name: database.py
Description: This script sets up the connection to a SQL database using SQLModel.
 It includes a Database class to manage the database connection and session.
 It also initializes the database and provides a session for FastAPI to use.
Author: MathTeixeira
Date: July 6, 2024
Version: 4.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from sqlmodel import SQLModel, Session, create_engine
from core.config import sql


class SqlDatabase:
  """
  Database class to manage the connection to the PostgreSQL database and provide
  methods to initialize the database and get a session.

  Attributes:
    userName (str): Database username.
    password (str): Database password.
    host (str): Database host.
    port (str): Database port.
    dbName (str): Database name.
    DATABASE_URL (str): Full database URL.
    engine (Engine): SQLAlchemy engine connected to the PostgreSQL database.
  """

  def __init__(self,
               userName: str = sql.USERNAME,
               password: str = sql.PASSWORD,
               host: str = sql.HOST,
               port: str = sql.PORT,
               dbName: str = sql.NAME):
    """
    Initialize the Database class with the provided configuration values.

    Args:
      userName (str): Database username.
      password (str): Database password.
      host (str): Database host.
      port (str): Database port.
      dbName (str): Database name.
    """
    self.userName = userName
    self.password = password
    self.host = host
    self.port = port
    self.dbName = dbName

    self.DATABASE_URL = f"postgresql://{self.userName}:{self.password}@{self.host}:{self.port}/{self.dbName}"
    self.engine = create_engine(self.DATABASE_URL)

  def init(self):
    """
    Initialize the database by creating all the tables defined in the SQLModel metadata.
    FastAPI will call this method to create the database tables.
    """
    SQLModel.metadata.create_all(self.engine)

  def getSession(self):
    """
    Provide a database session. This method is used as a dependency in FastAPI to ensure
    that each request has its own database session.

    Yields:
      session (Session): The database session.
    """
    # Session wraps the database connection and transaction, ensuring that the
    # changes are committed to the database at once, if no errors occur.
    # No partial changes are committed to the database.
    with Session(self.engine) as session:
      yield session


sqlDb = SqlDatabase()
