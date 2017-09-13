#!/usr/bin/python3
"""
View for States that handles all RESTful API actions
"""

from flask import jsonify, request, abort
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states_all():
    """ returns list of all State objects """
    states_all = []
    states = storage.all("State").values()
    for state in states:
        states_all.append(state.to_json())
    return jsonify(states_all)


@app_views.route('/states/<state_id>', methods=['GET'])
def state_get(state_id):
    """ handles GET method """
    try:
        state = storage.get("State", state_id)
        state = state.to_json()
        return jsonify(state)
    except:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def state_delete(state_id):
    """ handles DELETE method """
    try:
        empty_dict = {}
        state = storage.get("State", state_id)
        storage.delete(state)
        storage.save()
        return jsonify(empty_dict), 200
    except:
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def state_post():
    """ handles POST method """
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
    else:
        abort(400, "Not a JSON")
    if 'name' not in data:
        abort(400, "Missing name")
    state = State(**data)
    state.save()
    state = state.to_json()
    return jsonify(state), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def state_put(state_id):
    """ handles PUT method """
    try:
        state = storage.get("State", state_id)
    except:
        abort(404)
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
    else:
        abort(400, "Not a JSON")
    for key, value in data.items():
        ignore_keys = ["id", "created_at", "updated_at"]
        if key not in ignore_keys:
            state.bm_update(key, value)
    storage.save()
    state = state.to_json()
    return jsonify(state), 200