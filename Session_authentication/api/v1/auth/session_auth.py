#!/usr/bin/env python3
"""
SessionAuth module to manage session-based authentication.
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class to handle session authentication logic.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for the given user ID.

        Args:
            user_id (str): The ID of the user to create a session for.

        Returns:
            str: The created session ID, or None if user_id is None or invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        
        session_id = str(uuid.uuid4())  # Create a unique session ID
        self.user_id_by_session_id[session_id] = user_id  # Link the session ID with the user ID
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the user ID associated with a session ID.

        Args:
            session_id (str): The session ID to retrieve the user ID for.

        Returns:
            str: The user ID, or None if session_id is None or invalid.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """
        Retrieves the current authenticated user based on the session cookie.

        Args:
            request: The Flask request object that contains the session cookie.

        Returns:
            User: The authenticated User object if the session is valid.
            None: If the session ID is not valid or the session is not linked to any user.
        """
        session_id = self.session_cookie(request)
        
        if session_id is None:  # No cookie sent
            return None
        
        user_id = self.user_id_for_session_id(session_id)  # Retrieve the user ID from session ID
        
        if user_id is None:  # Cookie sent but not a valid session
            return None

        return User.get(user_id)  # Assuming you have a method `get` to retrieve a User by ID
