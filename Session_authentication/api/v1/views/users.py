from flask import jsonify, abort, request
from api.v1.views import app_views
from api.v1.auth.session_auth import SessionAuth

# Create an instance of SessionAuth
auth = SessionAuth()

class User:
    """A simple in-memory User model for demonstration purposes."""
    users = []  # In-memory list to hold user data

    def __init__(self, user_id, email, password):
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
            if user.id == int(user_id):
                return user
        return None

    @staticmethod
    def create(email, password):
        """Creates a new user."""
        new_id = len(User.users) + 1
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


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    GET /api/v1/users
    Retrieves the list of all User objects in the system.
    Requires Basic Authentication or Session Authentication.
    """
    users = User.get_all_users()
    if not users:
        abort(404, description="No users found")
    return jsonify([user.to_dict() for user in users]), 200


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    GET /api/v1/users/<user_id>
    Retrieves a specific User object by user ID.
    If the user_id is 'me', retrieve the authenticated user using session authentication.
    """
    if user_id == "me":
        current_user = auth.current_user(request)
        if current_user is None:
            abort(404, description="User not found")
        return jsonify(current_user.to_dict()), 200

    user = User.get_user_by_id(user_id)
    if user is None:
        abort(404, description=f"User with ID {user_id} not found")
    return jsonify(user.to_dict()), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
    POST /api/v1/users
    Creates a new User object.
    Requires Basic Authentication.
    """
    try:
        user_data = request.get_json()
        if (not user_data or 'email' not in user_data or
                'password' not in user_data):
            abort(400, description="Invalid JSON data")

        new_user = User.create(user_data['email'], user_data['password'])
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        abort(400, description=f"Error creating user: {str(e)}")


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """
    PUT /api/v1/users/<user_id>
    Updates an existing User object.
    Requires Basic Authentication or Session Authentication.
    """
    user = User.get_user_by_id(user_id)
    if user is None:
        abort(404, description=f"User with ID {user_id} not found")

    user_data = request.get_json()
    if not user_data:
        abort(400, description="Invalid JSON data")

    try:
        updated_user = user.update(**user_data)
        return jsonify(updated_user.to_dict()), 200
    except Exception as e:
        abort(400, description=f"Error updating user: {str(e)}")


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    DELETE /api/v1/users/<user_id>
    Deletes a User object by user ID.
    Requires Basic Authentication or Session Authentication.
    """
    user = User.get_user_by_id(user_id)
    if user is None:
        abort(404, description=f"User with ID {user_id} not found")

    try:
        user.delete()
        return jsonify({}), 200
    except Exception as e:
        abort(400, description=f"Error deleting user: {str(e)}")
