from flask import Blueprint, jsonify, abort, make_response

from .planets import Planet, planets_list
planets_bp = Blueprint("all_planets", __name__, url_prefix = "/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"massage":f"The planet_id {planet_id} is not valid."}, 400))
    
    for planet in planets_list:
        if planet.id == planet_id:
            return planet
    abort(make_response({"massage":f"The planet with id {planet_id} not exist."}, 404))

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    planets_response = []
    for planet in planets_list:
        planets_response.append(planet.convert_to_dict())
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_planet_by_id(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.convert_to_dict(), 200)
