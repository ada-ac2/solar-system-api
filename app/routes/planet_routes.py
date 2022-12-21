from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["POST"])
def create_planet():
    planet_value = request.get_json()
    new_planet = Planet(
                    name = planet_value["name"],
                    livable = planet_value["livable"],
                    number_of_moons = planet_value["number_of_moons"],
                    length_of_year = planet_value["length_of_year"],
                    namesake = planet_value["namesake"],
                    atmosphere = planet_value["atmosphere"], 
                    diameter = planet_value["diameter"],
                    description = planet_value["description"])

    if "name" not in planet_value \
        or "livable" not in planet_value \
        or "number_of_moons" not in planet_value \
        or "length_of_year" not in planet_value \
        or "namesake" not in planet_value \
        or "atmosphere" not in planet_value \
        or "diameter" not in planet_value \
        or "description" not in planet_value:
        return make_response(f"Invalid request", 400)

    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} succesfully created", 201)    

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    all_planets = Planet.query.all()
    planet_response = []
    for planet in all_planets:
        planet_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "livable": planet.livable,
                "number_of_moons": planet.number_of_moons,
                "length_of_year": planet.length_of_year,
                "namesake": planet.namesake,
                "atmosphere": planet.atmosphere,
                "diameter": planet.diameter,
                "description": planet.description
            })
    return jsonify(planet_response), 200

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_planet_by_id(planet_id):
#     planet = validate_planet(planet_id)
#     return jsonify(planet.convert_to_dict(), 200)
