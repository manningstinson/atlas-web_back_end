import uuid

class User:
    """A simple in-memory User model for demonstration purposes."""
    users = []  # In-memory list to hold user data

    def __init__(self, user_id, email, password):
        """
        Initializes a new user with an ID, email, and password.
        Args:
            user_id (str): The ID of the user (UUID).
            email (str): The email of the user.
            password (str): The password of the user.
        """
        self.id = user_id
        self.email = email
        self.password = password

    def to_dict(self):
        """Converts the user object to a dictionary."""
        return {
            "id": self.id,
            "email": self.email
        }

    @staticmethod
    def get_all_users():
        """Returns all users."""
        return User.users

    @staticmethod
    def get_user_by_id(user_id):
        """Returns a user by their ID."""
        for user in User.users:
            if user.id == user_id:  # Compare ID as string
                return user
        return None

    @staticmethod
    def create(email, password):
        """Creates a new user."""
        new_id = str(uuid.uuid4())  # Generate a string UUID for user ID
        new_user = User(new_id, email, password)
        User.users.append(new_user)
        return new_user

    def update(self, **kwargs):
        """Updates user details."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def delete(self):
        """Deletes the user."""
        User.users = [user for user in User.users if user.id != self.id]
