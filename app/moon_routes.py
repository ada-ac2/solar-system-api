from app import db
from app.models.moon import Moon
from app.models.planet import Planet
from app.planet_routes import validate_model
from flask import Blueprint, jsonify, abort, make_response, request

moon_bp = Blueprint("moon_bp", __name__, url_prefix="/moons")

@moon_bp.route("", methods=["POST"])
def create_one_moon():
    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)
    
    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} successfully created"), 201)

@moon_bp.route("", methods=["GET"])
def read_one_moon_by_name():
    
    moons_query = Moon.query
    name_query = request.args.get("name")
    if name_query:
        moons_query = moons_query.filter(Moon.name.ilike(f"%{name_query}%"))
    moons = moons_query.all()
    moons_response = []
    for moon in moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response)

@moon_bp.route("/<moon_id>", methods=["GET"])
def read_one_moon_by_id(moon_id):

    moon = validate_model(Moon, moon_id)
    return moon.to_dict()

@moon_bp.route("", methods=["GET"])
def read_all_moons():
    
    moons = Moon.query.all()

    moons_response = []
    for moon in moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response)

@moon_bp.route("/<planet_id>/moons", methods=["POST"])
def create_one_moon_with_planet_id(planet_id):

    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)
    new_moon.planet = planet
    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} by {new_moon.planet.name} successfully created"), 201)

@moon_bp.route("/<planet_id>/moons", methods=["GET"])
def read_all_moons_from_a_planet(planet_id):

    planet = validate_model(Planet, planet_id)

    moons_response = []
    for moon in planet.moons:
        moons_response.append(moon.to_dict())
        
    return jsonify(moons_response)

@moon_bp.route("/<moon_id>", methods=["DELETE"])
def delete_moon_by_id(moon_id):
    moon = validate_model(Moon,moon_id)

    db.session.delete(moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {moon.name} successfully deleted"))


