# -*- coding: utf-8 -*-
"""
File Name: __init__.py
Description: This module initializes and exports database instances for SQL and
 NoSQL databases.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55

This file imports and exports database instances for SQL and NoSQL databases.
The SQL database instance is pre-initialized, while the NoSQL database class is
 exported for on-demand instantiation.
"""

from .sqlDatabase import sqlDb
from .noSqlDatabase import NoSqlConnection, getNoSqlConn

__all__ = ['sqlDb', 'NoSqlConnection', 'getNoSqlConn']
