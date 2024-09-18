#!/usr/bin/env python3
""" Main 4 for testing SessionAuth """
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User
import uuid
from models.user import User  # Adjust this based on your file structure


# Initialize a Flask app
app = Flask(__name__)

# Create a test user
user_email = "bobsession@hbtn.io"
user_clear_pwd = "fake_password"
user_id = str(uuid.uuid4())  # Generate a unique ID for the user

# Create and save the user (positional arguments)
user = User(user_id, user_email, user_clear_pwd)
User.users.append(user)  # Manually adding user to in-memory storage
print(f"User ID: {user.id}, Email: {user.email}")  # Debugging print

# Create a session for the user
sa = SessionAuth()
session_id = sa.create_session(user.id)
print(f"User with ID: {user.id} has a Session ID: {session_id}")

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path to check session and return user based on session ID """
    request_user = sa.current_user(request)
    if request_user is None:
        return "No user found\n"
    return f"User found: {request_user.id}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
