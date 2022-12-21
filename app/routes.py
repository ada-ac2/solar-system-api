from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planets import Planet


# from .models.planets import Planet, planets_list
planets_bp = Blueprint("all_planets", __name__, url_prefix = "/planets")

@planets_bp.route("",methods=["POST"])
def add_new_planet():
    request_body = request.get_json()
    
    new_planet = Planet(
        id = request_body["id"],
        description = request_body["description"],
        name = request_body["name"],
        diameter = request_body["diameter"],
        atmosphere = request_body["atmosphere"])
   
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created.", 201)

   


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"massage":f"The planet_id {planet_id} is not valid."}, 400))
    
#     for planet in planets_list:
#         if planet.id == planet_id:
#             return planet
#     abort(make_response({"massage":f"The planet with id {planet_id} not exist."}, 404))

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name":planet.name,
            "atmosphere":planet.atmosphere,
            "diameter":planet.diameter,
            "description":planet.description
        })
    return jsonify(planets_response), 200

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_planet_by_id(planet_id):
#     planet = validate_planet(planet_id)
#     return jsonify(planet.convert_to_dict(), 200)
