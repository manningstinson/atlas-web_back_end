#!/usr/bin/env python3
"""
This module defines the BasicAuth class for handling Basic Authentication.
It extends the base Auth class.
"""
from api.v1.auth.auth import Auth
from api.models.user import User  # Corrected import path for User
import base64
from typing import Tuple


class BasicAuth(Auth):
    """
    BasicAuth class to handle Basic Authentication logic.
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization header.
        
        Args:
            authorization_header (str): The Authorization header.
        
        Returns:
            str: The Base64 encoded part of the header, or None.
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 encoded Authorization header.
        
        Args:
            base64_authorization_header (str): The Base64 encoded header.
        
        Returns:
            str: The decoded string, or None if invalid.
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None
        return decoded

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """
        Extracts the user credentials from the decoded Base64 header.
        
        Args:
            decoded_base64_authorization_header (str): Decoded Base64 string.
        
        Returns:
            tuple: A tuple containing the user email and password, or None.
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> User:
        """
        Retrieves a User instance from email and password.
        
        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.
        
        Returns:
            User: The User object if valid, or None.
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            print("Invalid email or password format")
            return None
        user = User.search({'email': user_email})
        print(f"User found: {user}")
        if user is None:
            print(f"No user found with email {user_email}")
            return None
        if not user.is_valid_password(user_pwd):
            print("Invalid password")
            return None
        print(f"Authenticated user: {user.email}")
        return user

    def current_user(self, request=None) -> User:
        """
        Retrieves the current authenticated user based on the request.
        
        Args:
            request: The Flask request object.
        
        Returns:
            User: The authenticated User object, or None.
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            print("No Authorization header found")
            return None
        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            print("Invalid Authorization header format")
            return None
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            print("Failed to decode Base64 Authorization header")
            return None
        email, password = self.extract_user_credentials(decoded_auth)
        if email is None or password is None:
            print("Failed to extract credentials from Authorization header")
            return None
        return self.user_object_from_credentials(email, password)
