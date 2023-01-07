from app import db
from flask import Blueprint, jsonify, abort, make_response, request 
from app.model.planet import Planet

planets_bp = Blueprint("planets_bp",__name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)
