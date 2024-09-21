# user.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User  # Ensure User is imported


class DB:
    """DB class that handles all database operations related to User."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)  # Drop tables (for dev)
        Base.metadata.create_all(self._engine)  # Create all tables
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        Args:
            email (str): The user's email.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The created User object.

        Raises:
            ValueError: If the email is already registered.
        """
        try:
            self.find_user_by(email=email)
            raise ValueError("email already registered")
        except NoResultFound:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
            self._session.refresh(new_user)
            return new_user
        except Exception as e:
            raise e

    def find_user_by(self, **kwargs) -> User:
        """
        Find the first user that matches the provided criteria.

        Args:
            **kwargs: Arbitrary keyword arguments to filter the user.

        Returns:
            User: The first User object that matches the criteria.

        Raises:
            NoResultFound: If no user matches the criteria.
            InvalidRequestError: If invalid query arguments are provided.
        """
        if not kwargs:
            raise InvalidRequestError("No arguments provided.")

        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("No user found with the provided args.")
        except InvalidRequestError as e:
            raise InvalidRequestError(f"Invalid query arguments: {e}")

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update user attributes.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: Arbitrary keyword arguments representing user attributes
                      to update.

        Raises:
            ValueError: If any of the provided attributes are invalid.
            NoResultFound: If no user with the provided user_id exists.
            InvalidRequestError: If invalid query arguments are provided.
        """
        user = self.find_user_by(id=user_id)

        valid_attributes = set
        (column.name for column in User.__table__.columns)

        for key, value in kwargs.items():
            if key not in valid_attributes:
                raise ValueError(f"'{key}' is not a valid attribute of User")
            setattr(user, key, value)

        self._session.commit()
