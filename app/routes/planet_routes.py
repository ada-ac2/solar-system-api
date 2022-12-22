from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

# Helper functions
# Validating the id of the planet: id needs to be int and exists the planet with the id.
# Returning the valid Planet instance if valid id
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"Planet {planet_id} invalid"}, 400))
    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message":f"Planet {planet_id} not found"}, 404))
    return planet

# Validating the user input to create or update the table planet
# Returning the valid JSON if valid input
def validate_input(planet_value):
    if "name" not in planet_value or not isinstance(planet_value["name"], str) \
        or "livable" not in planet_value or not isinstance(planet_value["livable"], bool) \
        or "number_of_moons" not in planet_value or not isinstance(planet_value["number_of_moons"], int) \
        or "length_of_year" not in planet_value or not isinstance(planet_value["length_of_year"], int) \
        or "namesake" not in planet_value or not isinstance(planet_value["namesake"], str) \
        or "atmosphere" not in planet_value or not isinstance(planet_value["atmosphere"], str) \
        or "diameter" not in planet_value or not isinstance(planet_value["diameter"], str) \
        or "description" not in planet_value or not isinstance(planet_value["description"], str):
        return abort(make_response(f"Invalid request", 400))  
    return planet_value

# Routes functions
# Creating new record in the database Planet
@planets_bp.route("", methods = ["POST"])
def create_planet():
    planet_value = validate_input(request.get_json())
    new_planet = Planet(
                    name = planet_value["name"],
                    livable = planet_value["livable"],
                    number_of_moons = planet_value["number_of_moons"],
                    length_of_year = planet_value["length_of_year"],
                    namesake = planet_value["namesake"],
                    atmosphere = planet_value["atmosphere"], 
                    diameter = planet_value["diameter"],
                    description = planet_value["description"])

    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} succesfully created", 201)    

# Get all planets info
# Return JSON list
@planets_bp.route("", methods = ["GET"])
def get_planets_query():
    planet_query = Planet.query
    planet_name_query = request.args.get("name")
    if planet_name_query:
        planet_query = planet_query.filter(Planet.name.ilike(f"%{planet_name_query}%"))


    sort_query = request.args.get("sort")
    if sort_query == "desc":
        planet_query = planet_query.order_by(Planet.name.desc()).all()
    elif sort_query == "asc":
        planet_query = planet_query.order_by(Planet.name).all()
    
    planet_response = []
    for planet in planet_query:
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

# Read one planet 
# Return one panet info in JSON format    
@planets_bp.route("/<planet_id>",methods=["GET"] )
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
                "id": planet.id,
                "name": planet.name,
                "livable": planet.livable,
                "number_of_moons": planet.number_of_moons,
                "length_of_year": planet.length_of_year,
                "namesake": planet.namesake,
                "atmosphere": planet.atmosphere,
                "diameter": planet.diameter,
                "description": planet.description
    }

# Update one planet
@planets_bp.route("/<planet_id>",methods=["PUT"] )
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = validate_input(request.get_json())

    planet.name = request_body["name"],
    planet.livable = request_body["livable"],
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