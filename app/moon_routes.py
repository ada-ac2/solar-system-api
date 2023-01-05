from app import db
from app.models.moon import Moon
from app.planet_routes import validate_model
from flask import Blueprint, jsonify, make_response, request

moons_bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

@moons_bp.route("", methods=["POST"])
def create_moon():
    moon_data = request.get_json()
    new_moon = Moon.from_dict(moon_data)

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"Moon {new_moon.name} created", 201)

@moons_bp.route("", methods=["GET"])  
def get_moons_optional_query():
    moon_query = Moon.query

    name_query = request.args.get("name")
    if name_query:
        moon_query = moon_query.filter(Moon.name.ilike(f"%{name_query}%"))

    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            moon_query = moon_query.order_by(Moon.size.desc())
        else:
            moon_query = moon_query.order_by(Moon.size.asc())

    moons = moon_query.all()
    moon_response = []
    for moon in moons:
        moon_response.append(moon.to_dict())

    return jsonify(moon_response)

@moons_bp.route("/<moon_id>", methods=["GET"])
def get_moon_by_id(moon_id):
    moon_to_return = validate_model(Moon, moon_id)

    return jsonify(moon_to_return.to_dict())

@moons_bp.route("/<moon_id>", methods=["PUT"])
def replace_moon_with_id(moon_id):
    moon_data = request.get_json()
    moon_to_update = validate_model(Moon, moon_id)

    moon_to_update.name = moon_data["name"],
    moon_to_update.size = moon_data["size"],
    moon_to_update.description = moon_data["description"],

    db.session.commit()

    return make_response(f"Moon {moon_to_update.name} updated", 200)

@moons_bp.route("/<moon_id>", methods=["DELETE"])
def delete_moons_by_id(moon_id):
    moon_to_delete = validate_model(Moon, moon_id)
    db.session.delete(moon_to_delete)
    db.session.commit()

    return make_response(f"Moon {moon_to_delete.name} deleted", 200)

