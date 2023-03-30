#!/usr/bin/python3
""" State view module"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from models.review import Review


@app_views.route('/places/<place_id>/reviews', strict_slashes=False)
def reviews_by_place(place_id):
    """Return all reviews for a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    # This next line of code needs improvement as it's not memory efficient
    # ? Why? Because it's getting all the reviews from the database
    # * it should get only the reviews for this place
    # reviews = storage.all(Review).values()
    # The above line of code can be improved by using the following line
    reviews = place.reviews
    # get only the reviews for this place
    # reviews = [review for review in place.reviews]
    return jsonify([review.to_dict()
                    for review in reviews if review.place_id == place_id]), 200


@app_views.route('/reviews/<review_id>', strict_slashes=False)
def get_review(review_id):
    """Return a review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict()), 200


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """Delete review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def add_review(place_id):
    """Add review to a place
    body of the request must be a JSON object containing user_id and text
    Args:
        place_id (id): place id to add the review to

    Returns:
        review: review added
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    user = storage.get(User, data['user_id'])
    if user is None:
        abort(404)
    if 'text' not in data:
        abort(400, description="Missing text")
    data['place_id'] = place_id
    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Update Review

    Args:
        review_id (str): uuid of the review to update
    """
    review = storage.get(Review, review_id)
    if review is None:
        # print(review)
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id',
                       'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
