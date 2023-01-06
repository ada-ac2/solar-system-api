from app import db
from app.models.moon import Moon
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
from .validate_routes import validate_model, validate_moon_user_input, validate_planet_user_input

moons_bp = Blueprint("moons_bp", __name__, url_prefix = "/moons")

#`/moons/<planet_id>/moons` with the POST 
# @moons_bp.route("/moons", methods=["POST"])
# def create_moon(planet_id):

#     planet = validate_model(Planet, planet_id)

#     request_body = request.get_json()
#     new_moon = Moon.from_dict(request_body)
#     new_moon.planet = planet

#     db.session.add(new_moon)
#     db.session.commit()

#     message = f"Moon {new_moon.name} created with Planet {planet.name}"
#     return make_response(jsonify(message), 201)

# Get all moons info 
# /moons
# Return JSON list
@moons_bp.route("", methods = ["GET"])
def get_all_moons_query():
    moon_query = Moon.query
    # Filtering by name (return all records which name contains planet_name_query)
    moon_name_query = request.args.get("name")

    if moon_name_query:
        moon_query = moon_query.filter(Moon.name.ilike(f"%{moon_name_query}%"))
    
    sort_by_name_query = request.args.get("sort_by_name")
    if sort_by_name_query == "desc":
        moon_query = moon_query.order_by(Moon.name.desc()).all()
    elif sort_by_name_query == "asc":
        moon_query = moon_query.order_by(Moon.name).all()

    moon_response = []
    for moon in moon_query:
        moon_response.append(moon.to_dict())

    return jsonify(moon_response), 200