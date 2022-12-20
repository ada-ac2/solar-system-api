from .models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response
# planets = [
#     Planet(1, "Mercury", "Mercury is the closest planet to the Sun.", 88, 0),
#     Planet(2, "Venus", "Venus is the hottest planet in the solar system.",225 ,0 ),
#     Planet(3, "Earth", "Our home planet.", 365,1),
#     Planet(4, "Mars", "Also known as Red planet.",687, 2),
#     Planet(5, "Jupiter","Largest planet in the solar system.",4333, 80),
#     Planet(6, "Saturn", "Only planet to have rings made of ice and rock.",10759, 83),
#     Planet(7, "Uranus", "Only planet with a 97 degree tilted axis.", 30687, 27),
#     Planet(8, "Neptune", "Blue ice giant" ,60190, 14 )
# ]

# planets_bp = Blueprint("planets", __name__,url_prefix="/planets")
# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(planet.to_dict())
        
#     return jsonify(planets_response),200

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return jsonify(planet.to_dict())

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} is invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} is not found"}, 404))