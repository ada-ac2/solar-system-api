from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# class Planet():
#     def __init__(self, id, name, description, diameter):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.diameter = diameter

    # def to_dict(self):
    #     return   {
    #             "id": self.id,
    #             "name": self.name,
    #             "description": self.description,
    #             "diameter": self.diameter
    #         }


# planets = [
#     Planet(id = 3, name = "Earth", description = "habitable", diameter = 12756),
#     Planet(id = 1, name = "Mercury", description = "inhabitable", diameter = 4879),
#     Planet(id = 4, name = "Mars", description = "inhabitable", diameter = 6792)
# ]

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"Planet {planet_id} is not an int."}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     planet_response = []
#     for planet in planets:
#         planet_response.append(planet.to_dict())

#     return jsonify(planet_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_planet_by_id(planet_id):
#     planet = validate_planet(planet_id)
#     return jsonify(planet.to_dict())    

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body or 'diameter_in_km' not in request_body:
        return make_response("Invalid Request", 400)

    new_planet = Planet(name = request_body["name"], 
                        description = request_body["description"], 
                        diameter_in_km = request_body["diameter_in_km"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "diameter_in_km": planet.diameter_in_km
        })
    return jsonify(planets_response)