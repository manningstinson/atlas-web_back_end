#!/usr/bin/env python3
"""
Main test file for DB.add_user
"""

from db import DB
from user import User

def main():
    """Main function to test the add_user method."""
    my_db = DB()

    # Add a user and test the result
    user = my_db.add_user("eggmin@eggsample.com", "hashedpwd")
    print(f"DB.add_user returns a user object: {isinstance(user, User)}")
    print(f"User email: {user.email}")
    print(f"User hashed_password: {user.hashed_password}")

if __name__ == "__main__":
    main()
