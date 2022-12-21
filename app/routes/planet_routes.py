from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["POST"])
def create_planet():
    planet_value = request.get_json()
    new_planet = Planet(
                name = planet_value["name"],
                    number_of_moons = planet_value["number_of_moons"],
                    length_of_year = planet_value["length_of_year"],
                    namesake = planet_value["namesake"],
                    atmosphere = planet_value["atmosphere"], 
                    diameter = planet_value["diameter"],
                    description = planet_value["description"])

    if "name" not in planet_value \
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
                "number_of_moons": planet.number_of_moons,
                "length_of_year": planet.length_of_year,
                "namesake": planet.namesake,
                "atmosphere": planet.atmosphere,
                "diameter": planet.diameter,
                "description": planet.description
            })
    return jsonify(planet_response), 200


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"Planet {planet_id} invalid"}, 400))
    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message":f"Planet {planet_id} not found"}, 404))
    return planet
    
# Read one planet    
@planets_bp.route("/<planet_id>",methods=["GET"] )
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
                "id": planet.id,
                "name": planet.name,
                "number_of_moons": planet.number_of_moons,
                "length_of_year": planet.length_of_year,
                "namesake": planet.namesake,
                "atmosphere": planet.atmosphere,
                "diameter": planet.diameter,
                "description": planet.description
    }

# update one planet
@planets_bp.route("/<planet_id>",methods=["PUT"] )
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    
    request_body = request.get_json()

    if "name" not in request_body \
        or "number_of_moons" not in request_body \
        or "length_of_year" not in request_body \
        or "namesake" not in request_body \
        or "atmosphere" not in request_body \
        or "diameter" not in request_body \
        or "description" not in request_body:
        return make_response(f"Invalid request", 400)

    planet.name = request_body["name"],
    planet.number_of_moons = request_body["number_of_moons"],
    planet.length_of_year = request_body["length_of_year"],
    planet.namesake = request_body["namesake"],
    planet.atmosphere = request_body["atmosphere"], 
    planet.meter = request_body["diameter"],
    planet.description = request_body["description"]
    
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully update.")
    
    # Delete one planet
@planets_bp.route("/<planet_id>",methods=["DELETE"] )
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully delete.")
