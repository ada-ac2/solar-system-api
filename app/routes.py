from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

list_planets = [
    Planet(1, "Mercury", "is the smallest planet in the Solar System", "gray"),
    Planet(3, "Earth", "The planet that we live on.", "blue")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in list_planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        })

    return jsonify(planets_response)