#!/usr/bin/env python3
"""
User model definition for managing user data in the 'users' table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model representing the 'users' table.

    Attributes:
        id (int): Primary key, auto-incrementing user ID.
        email (str): User's email address, must be unique and not null.
        hashed_password (str): User's hashed password, required for login.
        session_id (str): Nullable session ID for tracking user sessions.
        reset_token (str): Nullable token used for password reset requests.
    """

    __tablename__ = 'users'

    # Unique identifier for each user, serves as the primary key
    id = Column(Integer, primary_key=True)

    # Email address for the user, must be unique and non-null
    email = Column(String(250), nullable=False)

    # Hashed password for the user, non-nullable for security purposes
    hashed_password = Column(String(250), nullable=False)

    # Session ID, used to store current session information (nullable)
    session_id = Column(String(250), nullable=True)

    # Reset token for password recovery, can be null
    reset_token = Column(String(250), nullable=True)
