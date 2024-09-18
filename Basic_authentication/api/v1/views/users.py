from flask import jsonify, abort, request
from models.user import User  # Import the User model
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    GET /api/v1/users
    Retrieves the list of all User objects in the system.
    Requires Basic Authentication.
    """
    users = User.get_all_users()  # Replace with your actual logic for
    # retrieving users
    if not users:
        abort(404, description="No users found")  # Return 404 if no
    # users are found
    return jsonify([user.to_dict() for user in users]), 200  # Convert user
    # objects to dict


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    GET /api/v1/users/<user_id>
    Retrieves a specific User object by user ID.
    Requires Basic Authentication.
    """
    user = User.get_user_by_id(user_id)  # Replace with your actual logic
    # for retrieving a user
    if user is None:
        abort(404, description=f"User with ID {user_id} not found")
    return jsonify(user.to_dict()), 200  # Convert the user object to dict


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
    POST /api/v1/users
    Creates a new User object.
    Requires Basic Authentication.
    """
    try:
        user_data = request.get_json()
        if not user_data:
            abort(400, description="Invalid JSON data")

        # Create a new user object (replace with actual user creation logic)
        new_user = User.create(**user_data)
        return jsonify(new_user.to_dict()), 201
        # Return new user data with 201 status
    except Exception as e:
        abort(400, description=f"Error creating user: {str(e)}")


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """
    PUT /api/v1/users/<user_id>
    Updates an existing User object.
    Requires Basic Authentication.
    """
    user = User.get_user_by_id(user_id)
    if user is None:
        abort(404, description=f"User with ID {user_id} not found")

    user_data = request.get_json()
    if not user_data:
        abort(400, description="Invalid JSON data")

    try:
        updated_user = user.update(**user_data)
        # Replace with actual update logic
        return jsonify(updated_user.to_dict()), 200
    except Exception as e:
        abort(400, description=f"Error updating user: {str(e)}")


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    DELETE /api/v1/users/<user_id>
    Deletes a User object by user ID.
    Requires Basic Authentication.
    """
    user = User.get_user_by_id(user_id)
    if user is None:
        abort(404, description=f"User with ID {user_id} not found")

    try:
        user.delete()  # Replace with actual delete logic
        return jsonify({}), 200  # Return an empty response with 200 status
    except Exception as e:
        abort(400, description=f"Error deleting user: {str(e)}")
