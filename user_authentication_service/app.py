# app.py

import logging
import os
import uuid

from flask import (
    Flask,
    abort,
    jsonify,
    make_response,
    redirect,
    request,
)
from auth import Auth

app = Flask(__name__)

# Configure the Flask app using environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
debug_mode = os.getenv('DEBUG_MODE', 'False').lower() in ['true', '1', 't']

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Instantiate the Auth object
auth = Auth()


@app.route("/", methods=["GET"])
def home():
    """
    Home route that returns a welcome message.
    """
    logger.info("Home route accessed")
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"])
def register_user():
    """
    Register a new user.

    Expects form data with 'email' and 'password'.

    Returns:
        - 200: User successfully created.
        - 400: Email already registered or missing fields.
    """
    # Extract form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Validate input
    if not email or not password:
        logger.warning("Registration failed: Missing email or password")
        return jsonify({"message": "email and password are required"}), 400

    try:
        # Attempt to register the user using Auth
        user = auth.register_user(email, password)
        logger.info(f"User registered: {email}")
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError as ve:
        # Handle the case where the email is already registered
        logger.warning(f"Registration failed for {email}: {ve}")
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        # Handle unexpected exceptions
        logger.error(f"Unexpected error during registration for {email}: {e}")
        return jsonify({"message": "Internal server error"}), 500


@app.route("/sessions", methods=["POST"])
def login_user():
    """
    Authenticate a user and log them in.

    Expects form data with 'email' and 'password'.

    Returns:
        - 200: Login successful.
        - 401: Unauthorized (invalid credentials).
        - 400: Missing fields.
    """
    # Extract form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Validate input
    if not email or not password:
        logger.warning("Login failed: Missing email or password")
        return jsonify({"message": "email and password are required"}), 400

    # Validate login credentials using Auth
    if not auth.valid_login(email, password):
        logger.warning(f"Invalid login attempt for {email}")
        abort(401)

    try:
        # Create a new session
        session_id = auth.create_session(email)
        logger.info(f"User logged in: {email}, Session ID: {session_id}")

        # Create the JSON response
        response = jsonify({"email": email, "message": "logged in"})

        # Set the session_id cookie with secure flags
        response.set_cookie(
            "session_id",
            session_id,
            httponly=True,
            secure=True,
            samesite='Lax'
        )

        return response, 200
    except Exception as e:
        logger.error(f"Unexpected error during login for {email}: {e}")
        return jsonify({"message": "Internal server error"}), 500


@app.route("/sessions", methods=["DELETE"])
def logout_user():
    """
    Log out a user by destroying their session.

    Expects:
        - Cookie with key 'session_id'.

    Returns:
        - Redirect to GET / if logout is successful.
        - 403 Forbidden if session_id is invalid or does not exist.
    """
    # Retrieve the session_id from cookies
    session_id = request.cookies.get('session_id')

    # If session_id is not provided, respond with 403 Forbidden
    if not session_id:
        logger.warning("Logout failed: No session_id provided")
        abort(403)

    # Retrieve the user associated with the session_id using Auth
    user = auth.get_user_from_session_id(session_id)

    # If no user is found with the provided session_id, respond with 403 Forbidden
    if not user:
        logger.warning(f"Logout failed: Invalid session_id {session_id}")
        abort(403)

    try:
        # Destroy the user's session
        auth.destroy_session(user.id)
        logger.info(f"User logged out: {user.email}, Session ID: {session_id}")

        # Create a response that redirects to the home route
        response = make_response(redirect("/"))

        # Remove the session_id cookie by setting it to an empty value and expiring it
        response.set_cookie(
            "session_id",
            "",
            expires=0,
            httponly=True,
            secure=True,
            samesite='Lax'
        )

        return response
    except Exception as e:
        logger.error(f"Unexpected error during logout for {user.email}: {e}")
        return jsonify({"message": "Internal server error"}), 500


@app.route("/profile", methods=["GET"])
def user_profile():
    """
    Retrieve the profile of the logged-in user.

    Expects:
        - Cookie with key 'session_id'.

    Returns:
        - 200: JSON payload with user's email.
        - 403: Forbidden if session_id is invalid or does not exist.
    """
    # Retrieve the session_id from cookies
    session_id = request.cookies.get('session_id')

    # If session_id is not provided, respond with 403 Forbidden
    if not session_id:
        logger.warning("Profile access failed: No session_id provided")
        abort(403)

    # Retrieve the user associated with the session_id using Auth
    user = auth.get_user_from_session_id(session_id)

    # If no user is found with the provided session_id, respond with 403 Forbidden
    if not user:
        logger.warning(f"Profile access failed: Invalid session_id {session_id}")
        abort(403)

    # Respond with the user's email
    logger.info(f"Profile accessed for user: {user.email}")
    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """
    Generate a reset password token for the user.

    Expects:
        - Form data with 'email'.

    Returns:
        - 200: JSON payload with user's email and reset token.
        - 403: Forbidden if email is not registered.
    """
    # Extract form data
    email = request.form.get('email')

    # Validate input
    if not email:
        logger.warning("Reset password failed: Missing email")
        return jsonify({"message": "email is required"}), 400

    try:
        # Check if the email is registered
        user = auth.get_user_from_email(email)
        if not user:
            logger.warning(f"Reset password failed: Email not registered - {email}")
            abort(403)

        # Generate a reset token
        reset_token = auth.get_reset_password_token(email)
        logger.info(f"Reset token generated for user: {email}")

        # Respond with the reset token
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError as ve:
        logger.warning(f"Reset password failed for {email}: {ve}")
        abort(403)
    except Exception as e:
        logger.error(f"Unexpected error during reset password for {email}: {e}")
        return jsonify({"message": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
