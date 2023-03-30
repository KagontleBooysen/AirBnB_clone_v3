#!/usr/bin/python3
""" State view module"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', strict_slashes=False)
def users():
    """Return all states"""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', strict_slashes=False)
def get_user(user_id):
    """Return a state"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict()), 200


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """Delete state"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def add_user():
    """Add A state"""
    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()
    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password' not in data:
        abort(400, description="Missing password")
    user = User(**data)
    user.save()

    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def update_user(user_id):
    """Update a state"""
    if not request.is_json:
        abort(400, description="Not a JSON")
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
