from flask import Blueprint, jsonify


from .planets import *
planets_bp = Blueprint("all_planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    planets_response = []
    for planet in planets_list:
        planets_response.append({
                "id":planet.id,
                "name":planet.name,
                "atmosphere":planet.atmosphere,
                "diameter":planet.diameter,
                "description":planet.description
            })
    return jsonify(planets_response), 200