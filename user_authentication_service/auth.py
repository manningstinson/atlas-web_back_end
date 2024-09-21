# auth.py

from db import DB
from user import User  # Import the User class
import uuid
import bcrypt

class Auth:
    """Auth class to handle authentication-related operations."""
    
    def __init__(self):
        """Initialize Auth with a DB instance."""
        self._db = DB()
    
    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.
        
        Args:
            email (str): The user's email.
            password (str): The user's password.
        
        Returns:
            User: The created User object.
        
        Raises:
            ValueError: If the email is already registered.
        """
        try:
            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            return self._db.add_user(email, hashed_password)
        except Exception as e:
            # Assuming DB.add_user raises ValueError for duplicate emails
            raise ValueError("email already registered") from e
    
    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials.
        
        Args:
            email (str): The user's email.
            password (str): The user's password.
        
        Returns:
            bool: True if credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8'))
        except Exception:
            return False
    
    def create_session(self, email: str) -> str:
        """
        Create a new session for the user.
        
        Args:
            email (str): The user's email.
        
        Returns:
            str: The generated session ID.
        """
        user = self._db.find_user_by(email=email)
        session_id = str(uuid.uuid4())
        self._db.update_user(user.id, session_id=session_id)
        return session_id
    
    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Retrieve a user based on the session ID.
        
        Args:
            session_id (str): The session ID.
        
        Returns:
            User: The User object associated with the session ID.
        """
        if not session_id:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None
    
    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a user's session.
        
        Args:
            user_id (int): The user's ID.
        
        Returns:
            None
        """
        self._db.update_user(user_id, session_id=None)
    
    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a reset password token for the user.
        
        Args:
            email (str): The user's email.
        
        Returns:
            str: The generated reset token.
        
        Raises:
            ValueError: If the email is not registered.
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = str(uuid.uuid4())
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except Exception:
            raise ValueError("email not registered")
    
    def get_user_from_email(self, email: str) -> User:
        """
        Retrieve a user based on their email.
        
        Args:
            email (str): The user's email.
        
        Returns:
            User: The User object associated with the email.
        """
        try:
            return self._db.find_user_by(email=email)
        except Exception:
            return None
