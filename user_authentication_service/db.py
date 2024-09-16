#!/usr/bin/env python3
"""
Main file to test add_user method in DB class.
"""

from db import DB
from user import User  # Make sure to import the User model


def main():
    """Main function to test the add_user method."""
    my_db = DB()

    # Test adding a new user
    user = my_db.add_user("eggmin@eggsample.com", "hashedpwd")

    # Check if the returned user object has the correct attributes
    print(f"DB.add_user returns a user object: {isinstance(user, User)}")
    print(f"User email: {user.email}")
    print(f"User hashed_password: {user.hashed_password}")


if __name__ == "__main__":
    main()
