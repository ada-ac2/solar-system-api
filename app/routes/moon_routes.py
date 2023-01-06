from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from app.routes.routes_helper import validate_model

moons_bp = Blueprint("moons", __name__, url_prefix="/moons")

@moons_bp.route("", methods=["POST"])
def create_moon():
    moon_data = request.get_json()

    new_moon = Moon.from_dict(moon_data)

    #add new moon to db
    db.session.add(new_moon)
    #commit new moon to db
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} created."), 201)


@moons_bp.route("", methods=["GET"])
def get_all_moons():
    moons_query = Moon.query

    name_query = request.args.get("name")
    if name_query:
        moons_query = moons_query.filter(Moon.name.ilike(f"%{name_query}%"))

    sort_query = request.args.get("sort")
    if sort_query == "asc":
        moons_query = moons_query.order_by(Moon.name.asc())
    if sort_query == "desc":
        moons_query = moons_query.order_by(Moon.name.desc())

    moons = moons_query.all()

    moons_response = []
    for moon in moons:
        moons_response.append(moon.to_dict())
        
    return jsonify(moons_response)


@moons_bp.route("/<moon_id>", methods=["GET"])
def get_one_moon_by_id(moon_id):
    moon = validate_model(Moon, moon_id)
    return moon.to_dict()