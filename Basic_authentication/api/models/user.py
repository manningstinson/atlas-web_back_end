#!/usr/bin/env python3
"""
This module defines the User class, which simulates a user in the system.
The class includes methods for searching users by email, validating passwords,
and saving user data.
"""

class User:
    """
    User class representing a user in the system.
    """

    # Class-level "database" to simulate saving users
    _user_db = []

    def __init__(self):
        self.email = None
        self.password = None
        self.first_name = None
        self.last_name = None

    @staticmethod
    def search(query):
        """
        Simulate searching for a user by email.

        Args:
            query (dict): A dictionary containing the search query.
        
        Returns:
            User: A User object if found, None otherwise.
        """
        # Simulating a user lookup by email
        for user in User._user_db:
            if user.email == query.get('email'):
                return user
        return None

    def is_valid_password(self, password: str) -> bool:
        """
        Check if the provided password is valid for this user.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return self.password == password

    def display_name(self) -> str:
        """
        Return a display-friendly name for the user.

        Returns:
            str: The user's email, used here as a display name.
        """
        return self.email

    def save(self):
        """
        Simulate saving the user to a "database" (in this case, a list).
        """
        User._user_db.append(self)
