from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from .validate_routes import validate_model, validate_moon_user_input, validate_planet_user_input
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

# Routes functions
# Creating new planet
@planets_bp.route("", methods = ["POST"])
def create_planet():
    planet_value = validate_planet_user_input(request.get_json())
    new_planet = Planet.from_dict(planet_value)

    db.session.add(new_planet)
    db.session.commit()
    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)    

# Get all planets info
# Return JSON list
@planets_bp.route("", methods = ["GET"])
def get_planets_query():
    planet_query = Planet.query
    # Filtering by name (return all records which name contains planet_name_query)
    planet_name_query = request.args.get("name")

    if planet_name_query:
        planet_query = planet_query.filter(Planet.name.ilike(f"%{planet_name_query}%"))
    
    sort_by_name_query = request.args.get("sort_by_name")
    if sort_by_name_query == "desc":
        planet_query = planet_query.order_by(Planet.name.desc()).all()
    elif sort_by_name_query == "asc":
        planet_query = planet_query.order_by(Planet.name).all()

    sort_by_length_of_year_query = request.args.get("sort_by_length_of_year")
    if sort_by_length_of_year_query == "desc":
        planet_query = planet_query.order_by(Planet.length_of_year.desc()).all()
    elif sort_by_length_of_year_query == "asc":
        planet_query = planet_query.order_by(Planet.length_of_year).all() 
    
    planet_response = []
    for planet in planet_query:
        planet_response.append(planet.to_dict())

    return jsonify(planet_response), 200

# Read one planet 
# Return one planet info in JSON format    
@planets_bp.route("/<planet_id>",methods=["GET"] )
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

# Update one planet
@planets_bp.route("/<planet_id>",methods=["PUT"] )
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = validate_planet_user_input(request.get_json())

    planet.name = request_body["name"]
    planet.length_of_year = request_body["length_of_year"]
    planet.description = request_body["description"]
    
    db.session.commit()
    message = f"Planet {planet_id} successfully updated"
    return make_response(jsonify(message), 200)   
    
# Delete one planet and all the moons dependent of the planet
@planets_bp.route("/<planet_id>",methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    if len(planet.moons)>0:
        i = 0
        while i < len(planet.moons):
            moon_id = planet.moons[i].id
            moon = validate_model(Moon, moon_id)
            db.session.delete(moon)
            db.session.commit()
            i += 1

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {planet.id} successfully deleted"), 200)

# Add moon info to the planet using planet id 
@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def add_new_moon_to_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    moon = Moon.from_dict(request_body)
    #moon.planet = planet
    moon.planet_id = planet_id

    db.session.add(moon)
    db.session.commit()

    message = f"Moon {moon.name} added to the planet {planet.name}."
    return make_response(jsonify(message), 201)

# Get all moons info for chosen planet (by planet id)
@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def get_all_moons_for_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    moons_response = []
    for moon in planet.moons:
        moons_response.append(moon.to_dict())

    return jsonify(moons_response)

# Get moon by id 
# Return one moon info in JSON format    
@planets_bp.route("/<planet_id>/moons/<moon_id>",methods=["GET"] )
def get_one_moon(planet_id, moon_id):
    planet = validate_model(Planet, planet_id)   
    moon = validate_model(Moon, moon_id)
    return moon.to_dict()

# Update moon info (by moon_id) of the planet using planet_id
@planets_bp.route("/<planet_id>/moons/<moon_id>", methods=["POST"])
def update_moon_of_planet(planet_id, moon_id):

    planet = validate_model(Planet, planet_id)
    moon = validate_model(Moon, moon_id)

    request_body = validate_moon_user_input(request.get_json())
    
    moon.name = request_body["name"]
    moon.size = request_body["size"]
    moon.description = request_body["description"]
 
    db.session.commit()

    message = f"Moon {moon.id} of the planet {planet.name} successfully updated."
    return make_response(jsonify(message), 201)

# Delete moon of the specific planet (using planet_id and moon_id)
@planets_bp.route("/<planet_id>/moons/<moon_id>", methods=["DELETE"])
def delete_moon_of_planet(planet_id, moon_id):

    planet = validate_model(Planet, planet_id)
    moon = validate_model(Moon, moon_id)

    db.session.delete(moon)
    db.session.commit()

    message = f"Moon {moon.id} of the planet {planet.name} successfully deleted."
    return make_response(jsonify(message), 201)