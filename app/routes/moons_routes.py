from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from ..models.moon import Moon
from ..models.planet import Planet
from app.routes.planets_routes import validate_model
moons_bp = Blueprint("moons", __name__, url_prefix = "/moons")

# ~~~~~~ Planet Routes ~~~~~
@moons_bp.route("", methods=["GET"])
def display_all_moons():
    moons = Moon.query.all()
    # fill http response
    response_moons = []
    for moon in moons:
        response_moons.append(moon.to_dict())  
    return jsonify(response_moons)

@moons_bp.route("/<moon_id>",methods=["GET"])
def display_moon(moon_id):
    moon = validate_model(Moon, moon_id)
    return moon.to_dict()


@moons_bp.route("", methods=["POST"])
def create_moon():
    request_body = request.get_json()

    #required request body: name, description, size, discovery_date, planet_id
    attribute_requirements = ["name", "description", "size", "discovery_date", "planet_id"]

    for req in attribute_requirements:
        if req not in request_body:
            abort(make_response({
                "message" : f"Failed to create a planet because {req} missing"
                }, 400))
    
    planet_id = request_body["planet_id"] 
    planet = validate_model(Planet, planet_id)
    new_moon = Moon.from_dict(request_body, planet, planet_id)
    db.session.add(new_moon)
    db.session.commit()
    return make_response({"message": "moon has been created successfully"}, 201)