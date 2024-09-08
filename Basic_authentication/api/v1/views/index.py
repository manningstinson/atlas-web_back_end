#!/usr/bin/env python3
"""
This module defines view functions for testing unauthorized and
forbidden routes in the API.
"""
from flask import Blueprint, abort

# Blueprint definition
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API."""
    return {"status": "OK"}

@app_views.route('/unauthorized', methods=['GET'])
def unauthorized_route():
    """Raises a 401 Unauthorized error."""
    abort(401)

@app_views.route('/forbidden', methods=['GET'])
def forbidden_route():
    """Raises a 403 Forbidden error."""
    abort(403)
