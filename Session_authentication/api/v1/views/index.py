#!/usr/bin/env python3
"""
This module defines view functions for testing unauthorized and
forbidden routes in the API.
"""
from flask import Blueprint, abort, request, jsonify
from api.v1.auth.session_auth import SessionAuth
from models.user import User
from flask import make_response
import os

# Blueprint definition
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Create a SessionAuth instance
auth = SessionAuth()

@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API."""
    return {"status": "OK"}


@app_views.route('/unauthorized/', methods=['GET'])
def unauthorized_route():
    """Raises a 401 Unauthorized error."""
    abort(401)


@app_views.route('/forbidden/', methods=['GET'])
def forbidden_route():
    """Raises a 403 Forbidden error."""
    abort(403)


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handle user login and create a session.
    Returns a session ID in a cookie.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Search for user by email
    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    # Check if the password is correct
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session and set the cookie
    session_id = auth.create_session(user.id)
    response = make_response(user.to_json())
    response.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Handle user logout and destroy the session.
    """
    if not auth.destroy_session(request):
        return abort(404)

    return jsonify({}), 200
