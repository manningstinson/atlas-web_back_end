#!/usr/bin/env python3
"""
This module defines a Flask application that manages basic authentication
and error handling. The application provides endpoints to check the API's
status and includes custom error handling for unauthorized (401) and
forbidden (403) requests.

The following features are included:
- Basic Authentication and handling of various authentication types
- Custom error handling for unauthorized and forbidden responses
- Pre-request processing to enforce authentication for certain routes
"""

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
import os

# Initialize the Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for the Flask app
CORS(app)

# Determine the authentication type (basic or none) based on environment variables
auth = None
AUTH_TYPE = os.getenv('AUTH_TYPE')
if AUTH_TYPE == 'basic_auth':
    auth = BasicAuth()
else:
    auth = Auth()

@app.route('/api/v1/status/', methods=['GET'])
def status():
    """
    Endpoint to check the status of the API.
    This route returns a simple JSON response indicating that the API is running.

    Returns:
        A JSON object containing the status message.
    """
    return jsonify({"status": "OK"})

@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_route():
    """
    Test endpoint to raise a 401 Unauthorized error.
    This route is used to simulate an unauthorized access attempt.

    Raises:
        401 HTTP error with a custom error handler.
    """
    abort(401)

@app.route('/api/v1/forbidden', methods=['GET'])
def forbidden_route():
    """
    Test endpoint to raise a 403 Forbidden error.
    This route is used to simulate a forbidden access attempt.

    Raises:
        403 HTTP error with a custom error handler.
    """
    abort(403)

@app.errorhandler(401)
def unauthorized(error):
    """
    Custom error handler for 401 Unauthorized errors.

    Args:
        error: The error object triggered when a 401 error is raised.

    Returns:
        A JSON response with an "Unauthorized" error message and status code 401.
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error):
    """
    Custom error handler for 403 Forbidden errors.

    Args:
        error: The error object triggered when a 403 error is raised.

    Returns:
        A JSON response with a "Forbidden" error message and status code 403.
    """
    return jsonify({"error": "Forbidden"}), 403

@app.before_request
def before_request_func():
    """
    Function executed before each request to handle authorization checks.
    This function determines if the request requires authentication and checks
    for valid authorization headers and a valid user. It enforces authentication
    for all routes except those specified in `excluded_paths`.

    If authentication is required but missing, it raises a 401 Unauthorized error.
    If the user is not valid, it raises a 403 Forbidden error.

    Raises:
        401 HTTP error if no Authorization header is present when required.
        403 HTTP error if the user cannot be authenticated.
    """
    if auth:
        # Define routes that do not require authentication
        excluded_paths = [
            '/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/'
        ]
        # Check if the current route requires authentication
        if not auth.require_auth(request.path, excluded_paths):
            return
        # Verify that the request contains a valid authorization header
        if auth.authorization_header(request) is None:
            abort(401)
        # Verify that the request is associated with a valid user
        if auth.current_user(request) is None:
            abort(403)

if __name__ == "__main__":
    """
    Main entry point of the application.
    Starts the Flask application, binding it to the host and port specified
    in environment variables or defaults to '0.0.0.0' and '5000'.
    """
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
