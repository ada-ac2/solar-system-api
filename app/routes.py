from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    planet_data = request.get_json()

    new_planet = Planet(
        name = planet_data["name"],
        description = planet_data["description"],
        orbit_days = planet_data["orbit_days"],
        num_moons = planet_data["num_moons"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} created", 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    all_planets = Planet.query.all()
    planet_response = []
    for planet in all_planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "orbit_days": planet.orbit_days,
            "num_moons": planet.num_moons
        })
    return jsonify(planet_response)







# 
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