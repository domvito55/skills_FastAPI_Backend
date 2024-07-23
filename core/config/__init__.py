# -*- coding: utf-8 -*-
"""
File Name: __init__.py
Description: This module initializes and exports configuration instances for various components.
Author: MathTeixeira
Date: July 11, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55

This file imports and exports configuration instances for SQL, AWS, Ideation, and NoSQL components.
These instances are created using the singleton pattern implemented in their respective modules.
"""

from .sqlConfig import sql
from .awsConfig import aws
from .ideationConfig import ideation
from .noSqlConfig import noSql
from .pageBPConfig import pageBP

__all__ = ['sql', 'aws', 'ideation', 'noSql', pageBP]
