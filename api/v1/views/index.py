#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models import state, city, place, review, user, amenity


@app_views.route('/status', methods=['GET', 'HEAD'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    function to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            amenity.Amenity: "amenities",
            city.City: "cities",
            place.Place: "places",
            review.Review: "reviews",
            state.State: "states",
            user.User: "users"
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
