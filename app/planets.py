from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [
    Planet(id = 3, name = "Earth", description = "habitable"),
    Planet(id = 1, name = "Mercury", description = "inhabitable"),
    Planet(id = 4, name = "Mars", description = "inhabitable")
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])

def get_all_planets():
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        })

    return jsonify(planet_response)