from flask import Blueprint, jsonify, abort, make_response

class Planet():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self):
        return   {
                "id": self.id,
                "name": self.name,
                "description": self.description
            }


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
        planet_response.append(planet.to_dict())

    return jsonify(planet_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet_by_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} is not an int."}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return jsonify(planet.to_dict())
            
    abort(make_response({"message":f"planet {planet_id} not found"}, 404))