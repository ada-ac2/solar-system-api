from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from app.planets_routes import validate_model
from app.models.moon import Moon
from flask import Blueprint, jsonify, abort, make_response, request

moons_bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

@moons_bp.route("", methods=["POST"])
def create_moon():
    moon_data = request.get_json()
    new_moon = Moon.from_dict(moon_data)
    
    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.id} successfully created"), 201)

@moons_bp.route("", methods=["GET"])
def get_all_moons():
    moons = Moon.query.all()

    moons_response = []
    for moon in moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response)
