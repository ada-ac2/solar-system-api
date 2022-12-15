from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

    def convert_planet_to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "color": self.color
        }

list_planets = [
    Planet(1, "Mercury", "is the smallest planet in the Solar System", "gray"),
    Planet(3, "Earth", "The planet that we live on.", "blue")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in list_planets:
        planets_response.append(planet.convert_planet_to_dict())

    return jsonify(planets_response)


def validate_id_return_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet_id {planet_id} invalid."},400))

    for planet in list_planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet_id {planet_id} not found."},404))

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet_by_id(planet_id):
    planet = validate_id_return_planet(planet_id)
    return planet.convert_planet_to_dict()
