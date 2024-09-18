#!/usr/bin/env python3
"""
This module defines the base authentication class used for managing
authorization and user authentication in the API.
"""
from flask import request
from typing import List, TypeVar
import os  # Import to access environment variables

class Auth:
    """
    Auth class to handle the basic authorization mechanism.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths excluded from auth.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path.rstrip('/')
        return path not in [p.rstrip('/') for p in excluded_paths]

    def authorization_header(self, request=None) -> str:
        """
        Extracts the Authorization header from the incoming request.

        Args:
            request: The Flask request object.

        Returns:
            str: The value of the Authorization header, or None.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder for retrieving the current authenticated user.

        Args:
            request: The Flask request object.

        Returns:
            User: None, to be implemented in subclasses.
        """
        return None

    def session_cookie(self, request=None) -> str:
        """
        Returns the value of the session cookie from the request.

        Args:
            request: The Flask request object.

        Returns:
            str: The value of the session cookie, or None if not found.
        """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME')  # Get the session cookie name from the environment
        if session_name is None:
            return None

        return request.cookies.get(session_name)
