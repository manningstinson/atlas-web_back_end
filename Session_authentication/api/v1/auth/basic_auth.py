#!/usr/bin/env python3
"""
This module defines the BasicAuth class for handling Basic Authentication.
It extends the base Auth class, which provides the base functionality for
authentication methods. The BasicAuth class specifically implements Basic
HTTP Authentication, allowing for the extraction and validation of user
credentials encoded in Base64 format.
"""

import sys
import os
import base64
from typing import Tuple, Optional

# Add the path to api directory for module imports
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../..')))

from api.models.user import User  # Adjusted the import path for User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class to handle Basic Authentication logic.

    This class is responsible for:
    - Extracting the Base64-encoded authorization header.
    - Decoding Base64 credentials.
    - Validating user credentials (email and password).
    - Fetching the authenticated user.
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> Optional[str]:
        """
        Extracts the Base64 part of the Authorization header.

        Args:
            authorization_header (str): The HTTP Authorization header
            provided by the client.

        Returns:
            str: The Base64 encoded part of the header (the credentials
            after "Basic ").
            None: If the Authorization header is missing, is not a string,
            or doesn't start with 'Basic '.
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> Optional[str]:
        """
        Decodes the Base64 encoded Authorization header.

        Args:
            base64_authorization_header (str): The Base64 encoded
            Authorization header.

        Returns:
            str: The decoded string containing the user credentials
            (email:password).
            None: If the header is invalid, not a string, or not
            Base64-decodable.
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
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        Extracts the user credentials (email and password) from the
        decoded Base64 string.

        Args:
            decoded_base64_authorization_header (str): The decoded Base64
            string containing 'email:password'.

        Returns:
            tuple: A tuple containing the user email and password as
            strings.
            None: If the string doesn't contain a colon or is invalid.
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> Optional[User]:
        """
        Retrieves a User instance from the provided email and password.

        Args:
            user_email (str): The email of the user.
            user_pwd (str): The password of the user.

        Returns:
            User: The User object if the email and password match a valid
            user in the system.
            None: If the email or password is invalid, or the user is not
            found.
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        user = User.search({'email': user_email})
        if user is None:
            return None

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> Optional[User]:
        """
        Retrieves the current authenticated user based on the request.

        This method extracts the authorization header from the request,
        decodes the Base64 encoded credentials, and validates them to
        return the corresponding User object.

        Args:
            request (Flask request object, optional): The incoming request
            object that contains the Authorization header.

        Returns:
            User: The authenticated User object if valid credentials are
            provided.
            None: If the Authorization header is missing, invalid, or the
            credentials are incorrect.
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None

        email, password = self.extract_user_credentials(decoded_auth)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
