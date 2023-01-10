from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets_bp", __name__,url_prefix="/planets")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    if "name" not in request_body:
        return make_response("Invalid Request", 400)

    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()
    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planet_query = Planet.query

    name_query = request.args.get("name")
    if name_query:
        planet_query = planet_query.filter(Planet.name.ilike(f"%{name_query}%"))
        
    sort_query = request.args.get("sort")
    if sort_query == "desc":
        planet_query = planet_query.order_by(Planet.name.desc())
    else: 
        planet_query = planet_query.order_by(Planet.name)
    
        
    planets = planet_query.all()
        
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.orbit_days = request_body["orbit_days"]
    planet.num_moons = request_body["num_moons"]

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully updated"))

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully deleted"))

@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def create_one_moon_with_planet_id(planet_id):

    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)
    new_moon.planet = planet
    db.session.add(new_moon)
    planet.num_moons = len(planet.moons)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} by {new_moon.planet.name} successfully created"), 201)

@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def read_all_moons_from_a_planet(planet_id):

    planet = validate_model(Planet, planet_id)

    moons_response = []
    for moon in planet.moons:
        moons_response.append(moon.to_dict())
        
    return jsonify(moons_response)