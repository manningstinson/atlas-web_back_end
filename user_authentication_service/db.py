#!/usr/bin/env python3
"""
DB module for managing database operations related to users.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import User, Base

class DB:
    """DB class to manage the database for user operations."""

    def __init__(self) -> None:
        """
        Initialize a new DB instance.
        Creates the 'users' table if it doesn't exist and sets up the session.
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.create_all(self._engine)  # Create the tables if they don't exist
        self.__session = None  # Session is initially None

    @property
    def _session(self):
        """
        Return a memoized session object.
        Creates a session if it doesn't exist.
        
        Returns:
            Session: A SQLAlchemy session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()  # Instantiate a new session
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        Args:
            email (str): The user's email address.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The newly created User object.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)  # Add the user to the session
        self._session.commit()  # Commit the session to the database
        self._session.refresh(user)  # Refresh the user instance to reflect any updates (like ID)
        return user  # Return the newly created User object
