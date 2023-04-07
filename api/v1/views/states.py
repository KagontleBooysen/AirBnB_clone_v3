#!/usr/bin/python3
""" State view module"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State

"""Return all states
    ---
    parameters:
      - name: parameter_name
        in: formData
        type: string
        required: true
        description: Description of the parameter
    responses:
      200:
        description: Success message
        schema:
          type: string
          example: 'Success!'
    """


@app_views.route('/states', strict_slashes=False)
def states():
    """Return all states
    ---
    responses:
        200:
            description: A list of all states
            schema:
                type: array
                example: [
                            {
                                "__class__": "State",
                                "created_at": "2023-04-07T13:10:30.674190",
                                "id": "db28ac2f-fb15-439b-9bde-c80b680a8ac6",
                                "updated_at": "2023-04-07T13:10:30.674190"
                            }
                            ]
    """
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state(state_id):
    """Return a state
    ---
    responses:
        200:
            description: A state with the given id
            schema:
                type: object
                example: {"__class__": "State",
                "created_at": "2023-04-07T13:10:30.674190",
                "id": "db28ac2f-fb15-439b-9bde-c80b680a8ac6",
                "updated_at": "2023-04-07T13:10:30.674190"}
        404:
            error: state not found
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict()), 200


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """Delete a state
    ---
    response:
        200:
            description: empty object
            example: {}
        404:
            description: state not found
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def add_state():
    """Add A state"""
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
