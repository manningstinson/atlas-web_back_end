#!/usr/bin/env python3
"""
SessionAuth module to manage session-based authentication.
"""
import os
import uuid
from models.user import User
from api.v1.auth.auth import Auth

class SessionAuth(Auth):
    """
    SessionAuth class to handle session authentication logic.

    This class is responsible for:
    - Creating and managing session IDs.
    - Storing session-user associations.
    - Fetching authenticated users based on session cookies.
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

        session_id = str(uuid.uuid4())  # Generate a new session ID
        self.user_id_by_session_id[session_id] = user_id  # Store the session-user association
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

        This method extracts the session ID from the request cookie and
        returns the corresponding User object.

        Args:
            request (Flask request object, optional): The incoming request
            object that contains the session cookie.

        Returns:
            User: The authenticated User object if a valid session is found.
            None: If the session ID is missing, invalid, or the session is not found.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)  # Assuming you have a method to get User by ID in your User model

    def destroy_session(self, request=None) -> bool:
        """
        Deletes the user session / logs out the user.

        Args:
            request (Flask request object, optional): The incoming request
            object that contains the session cookie.

        Returns:
            bool: True if the session was successfully deleted, False otherwise.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        if session_id not in self.user_id_by_session_id:
            return False

        del self.user_id_by_session_id[session_id]  # Remove the session
        return True

    def session_cookie(self, request=None) -> str:
        """
        Extracts the session ID from the session cookie.

        Args:
            request: The Flask request object.

        Returns:
            str: The session ID, or None if not found.
        """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME')  # Get the cookie name from environment variable
        return request.cookies.get(session_name)
