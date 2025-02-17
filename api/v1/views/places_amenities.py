#!/usr/bin/python3
'''
    RESTful API for linking Place and Amenity objects
'''
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.amenity import Amenity


@app_views.route('/places/<place_id>/amenities', methods=['GET'], strict_slashes=False)
def get_place_amenities(place_id):
    '''
        Retrieves the list of all Amenity objects of a Place
    '''
    place_obj = storage.get(Place, place_id)

    if place_obj is None:
        abort(404)

    amenities = [amenity.to_dict() for amenity in place_obj.amenities]
    return jsonify(amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    '''
        Deletes an Amenity object from a Place
    '''
    place_obj = storage.get(Place, place_id)
    amenity_obj = storage.get(Amenity, amenity_id)

    if place_obj is None or amenity_obj is None:
        abort(404)

    if amenity_obj not in place_obj.amenities:
        abort(404)

    place_obj.amenities.remove(amenity_obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'], strict_slashes=False)
def link_place_amenity(place_id, amenity_id):
    '''
        Links an Amenity object to a Place
    '''
    place_obj = storage.get(Place, place_id)
    amenity_obj = storage.get(Amenity, amenity_id)

    if place_obj is None or amenity_obj is None:
        abort(404)

    if amenity_obj in place_obj.amenities:
        return jsonify(amenity_obj.to_dict()), 200

    place_obj.amenities.append(amenity_obj)
    storage.save()
    return jsonify(amenity_obj.to_dict()), 201

