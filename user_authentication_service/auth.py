# auth.py

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.exc import IntegrityError

class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    # Task 4: Hash password
    def _hash_password(self, password: str) -> bytes:
        """
        Hash a password using bcrypt's hashpw method with a generated salt.

        Args:
        password (str): The password to hash.

        Returns:
        bytes: The salted hash of the password.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Task 5: Register user
    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the given email and password.

        Args:
        email (str): The user's email.
        password (str): The user's password.

        Returns:
        User: The created User object.

        Raises:
        ValueError: If the user with the given email already exists.
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except Exception:
            pass  # Proceed if no user is found
        
        hashed_password = self._hash_password(password)
        new_user = self._db.add_user(email=email, hashed_password=hashed_password)
        return new_user

    # Task 8: Credentials validation
    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate the user credentials.

        Args:
        email (str): The user's email.
        password (str): The user's password.

        Returns:
        bool: True if the credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except Exception:
            return False

        return False

    # Task 9: Generate UUID
    def _generate_uuid(self) -> str:
        """
        Generate a new UUID and return it as a string.

        Returns:
        str: A string representation of a new UUID.
        """
        return str(uuid.uuid4())

    # Task 10: Create session
    def create_session(self, email: str) -> str:
        """
        Create a session ID for the user corresponding to the given email.

        Args:
        email (str): The user's email.

        Returns:
        str: The session ID as a string, or None if the user is not found.
        """
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                return None
            
            session_id = self._generate_uuid()
            self._db.update_user(user.id, {"session_id": session_id})
            return session_id
        except Exception:
            return None

    # Task 12: Find user by session ID
    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Retrieve a user by their session ID.

        Args:
        session_id (str): The session ID.

        Returns:
        User: The user corresponding to the session ID, or None if no user is found.
        """
        if session_id is None:
            return None
        
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    # Task 13: Destroy session
    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a session by setting the user's session_id to None.

        Args:
        user_id (int): The user's ID.

        Returns:
        None
        """
        try:
            self._db.update_user(user_id, {"session_id": None})
        except Exception:
            pass  # Ignore errors while destroying session

    # Task 16: Generate reset password token
    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a reset password token for the user identified by email.

        Args:
        email (str): The user's email.

        Returns:
        str: The reset password token.

        Raises:
        ValueError: If the user with the given email does not exist.
        """
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                raise ValueError(f"User with email {email} does not exist")
            
            reset_token = self._generate_uuid()
            self._db.update_user(user.id, {"reset_token": reset_token})
            return reset_token
        except Exception:
            raise ValueError(f"User with email {email} does not exist")

    # Task 18: Update password
    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update the password of the user identified by the reset_token.

        Args:
        reset_token (str): The reset token.
        password (str): The new password.

        Returns:
        None

        Raises:
        ValueError: If the reset token is invalid.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if not user:
                raise ValueError("Invalid reset token")
            
            hashed_password = self._hash_password(password)
            self._db.update_user(user.id, {"hashed_password": hashed_password, "reset_token": None})
        except Exception:
            raise ValueError("Invalid reset token")
