# -*- coding: utf-8 -*-
"""
Package Name: core
Description: This package contains the core modules for the application.
Author: MathTeixeira
Date: July 9, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55

This package includes configuration modules and database interfaces for both SQL
 and NoSQL databases. It provides centralized access to configuration settings
 and database connections used throughout the application.
"""

from .config import aws, ideation, sql, noSql
from .database.sqlDatabase import sqlDb
from .database.noSqlDatabase import NoSqlConnection

__all__ = ['aws', 'ideation', 'sql', 'noSql', 'sqlDb', 'NoSqlConnection']
