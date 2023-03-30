#!/usr/bin/python3
""" State view module"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity


@app_views.route('/places/<place_id>/amenities', strict_slashes=False)
def get_amenities(place_id):
    """ Return a list of all amenities in a place

    Args:
        place_id (str): id of the place to get amenities from

    Returns:
        amenities : list of amenities in the place
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenities = place.amenities
    return jsonify([amenity.to_dict()
                    for amenity in amenities]), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 strict_slashes=False, methods=['DELETE'])
def delete_amenity(place_id, amenity_id):
    """ Delete an amenity from a place

    Args:
        place_id (str): id of the place to delete the amenity from
        amenity_id (str): id of the amenity to delete

    Returns:
        {} : empty dictionary with status code 200
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if amenity not in place.amenities:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 strict_slashes=False, methods=['POST'])
def link_amenity_to_place(place_id, amenity_id):
    """ Link an amenity to a place

    Args:
        place_id (str): id of the place to link the amenity to
        amenity_id (str): id of the amenity to link

    Returns:
        amenity : amenity linked to the place
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200
    place.amenities.append(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201
