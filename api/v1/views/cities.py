#!/usr/bin/python3
""" City view module"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State


@app_views.route('/cities', strict_slashes=False)
def cities():
    """Return all states"""
    cities = storage.all(City).values()
    return jsonify([city.to_dict() for city in cities])


@app_views.route('/states/<state_id>/cities', strict_slashes=False)
def cities_by_state(state_id):
    """Return all states"""
    cities = storage.all(City).values()
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = [city.to_dict() for city in cities if city.state_id == state_id]
    return jsonify(cities), 200


@app_views.route('/cities/<city_id>', strict_slashes=False)
def get_city(city_id):
    """ Return a city by id

    Args:
        city_id (str): city id

    Returns:
        city: json representation of the city
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict()), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Delete state"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({}), 200


# @app_views.route('/cities', methods=['POST'], strict_slashes=False)
# def add_city():
#     """Add A state"""
#     if not request.is_json:
#         abort(400, description="Not a JSON")
#     data = request.get_json()
#     if 'name' not in data:
#         abort(400, description="Missing name")
#     city = City(**data)
#     city.save()
#     return jsonify(city.to_dict()), 201


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def add_city_to_state(state_id):
    """Add A state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    city = City(**data)
    city.state_id = state_id
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Update city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200
