#!/usr/bin/env python3
"""
This module defines the User class, which simulates a user in the system.
The class includes methods for searching users by email and validating passwords.
"""

class User:
    """
    User class representing a user in the system.
    """

    def __init__(self):
        self.email = None
        self.password = None

    @staticmethod
    def search(query):
        """
        Simulate searching for a user by email.

        Args:
            query (dict): A dictionary containing the search query.
        
        Returns:
            User: A User object if found, None otherwise.
        """
        # Simulating a user lookup. Replace this with actual DB lookup logic if needed.
        if query.get('email') == 'bob@hbtn.io':
            user = User()
            user.email = 'bob@hbtn.io'
            user.password = 'H0lbertonSchool98!'  # Simulating stored password
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
