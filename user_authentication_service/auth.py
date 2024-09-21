import bcrypt
import uuid
from db import DB
from user import User

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

    # Task 9: Generate UUID (Private function, used only within the class)
    def _generate_uuid(self) -> str:
        """
        Generate a new UUID and return it as a string.

        Returns:
        str: A string representation of a new UUID.
        """
        return str(uuid.uuid4())

    # Task 10: Create session
    def create_session(self, email: str) -> str | None:
        """
        Create a session ID for the user corresponding to the given email.

        Args:
        email (str): The user's email.

        Returns:
        str: The session ID as a string, or None if the user is not found.
        """
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)
            if not user:
                return None
            
            # Generate a new session ID
            session_id = self._generate_uuid()
            
            # Update the user's session_id in the database
            self._db.update_user(user.id, {"session_id": session_id})
            
            return session_id
        except Exception as e:
            print(f"Error creating session: {e}")
            return None

    # Other methods from previous tasks can follow...
