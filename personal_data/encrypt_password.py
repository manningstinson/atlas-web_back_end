#!/usr/bin/env python3
"""
This module provides functions for hashing and validating passwords
using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with a random salt and returns the salted,
    hashed password.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: A salted, hashed password.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against its hashed version.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain text password to validate.

    Returns:
        bool: True if the password matches the hashed password,
        False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
