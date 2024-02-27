#!/usr/bin/python3
'''
    flask with general routes
    routes:
        /status:    display "status":"OK"
        /stats:     display total for all classes
        /api/v1/stats: display count of each object type
'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    '''
        return JSON of OK status
    '''
    return jsonify({'status': 'OK'})


@app_views.route("/stats")
def storage_counts():
    '''
        return counts of all classes in storage
    '''
    cls_counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(cls_counts)


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def object_counts():
    '''
        return count of each object type
    '''
    obj_counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(obj_counts)

