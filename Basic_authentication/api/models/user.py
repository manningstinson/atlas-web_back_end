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

    # Simulating an in-memory "database" for user storage
    _user_db = []

    def __init__(self):
        """
        Initializes a new User object with email, password, first_name, and last_name.
        """
        self.email = None
        self.password = None
        self.first_name = None
        self.last_name = None

    @staticmethod
    def search(query):
        """
        Simulate searching for a user by email.

        Args:
            query (dict): A dictionary containing the search query (email).
        
        Returns:
            User: A User object if found, None otherwise.
        """
        # Simulating a user lookup by email in the in-memory "_user_db"
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
        Simulate saving the user to the in-memory "database".
        If the user already exists (based on email), it updates the user details.
        """
        existing_user = User.search({'email': self.email})
        if not existing_user:
            # Add new user to the in-memory "database"
            User._user_db.append(self)
        else:
            # Update existing user's information
            existing_user.password = self.password
            existing_user.first_name = self.first_name
            existing_user.last_name = self.last_name

    @staticmethod
    def print_all_users():
        """
        Utility function to print all users in the in-memory "database".
        This is for debugging purposes.
        """
        for user in User._user_db:
            print(f"User: {user.email}, Password: {user.password}")
