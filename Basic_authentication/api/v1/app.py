#!/usr/bin/env python3
"""
This module defines a simple Flask application that handles basic
authentication and error handling. It includes endpoints for status,
unauthorized access, and forbidden access.
"""
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
import os

app = Flask(__name__)
CORS(app)

auth = None
AUTH_TYPE = os.getenv('AUTH_TYPE')
if AUTH_TYPE == 'basic_auth':
    auth = BasicAuth()
else:
    auth = Auth()

@app.route('/api/v1/status/', methods=['GET'])
def status():
    """Returns the status of the API."""
    return jsonify({"status": "OK"})

@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_route():
    """Raises a 401 Unauthorized error."""
    abort(401)

@app.route('/api/v1/forbidden', methods=['GET'])
def forbidden_route():
    """Raises a 403 Forbidden error."""
    abort(403)

@app.errorhandler(401)
def unauthorized(error):
    """Handles 401 Unauthorized errors."""
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error):
    """Handles 403 Forbidden errors."""
    return jsonify({"error": "Forbidden"}), 403

@app.before_request
def before_request_func():
    """
    Function that runs before each request to verify the authorization
    headers and user authentication if required for the path.
    """
    if auth:
        excluded_paths = [
            '/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/'
        ]
        if not auth.require_auth(request.path, excluded_paths):
            return
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)

if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
