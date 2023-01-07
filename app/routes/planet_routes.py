from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from app.routes.routes_helper import validate_model

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    planet_data = request.get_json()

    new_planet = Planet.from_dict(planet_data)

    #add new planet to db
    db.session.add(new_planet)
    #commit new planet to db
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} created."), 201)


@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_query = Planet.query

    name_query = request.args.get("name")
    if name_query:
        planets_query = planets_query.filter(Planet.name.ilike(f"%{name_query}%"))

    sort_query = request.args.get("sort")
    if sort_query == "asc":
        planets_query = planets_query.order_by(Planet.name.asc())
    if sort_query == "desc":
        planets_query = planets_query.order_by(Planet.name.desc())

    planets = planets_query.all()

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
        
    return jsonify(planets_response)

# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     planets = Planet.query.all()
#     planets_response = []

#     for planet in planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "color": planet.color
#         })

#    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet_by_id(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully updated."), 200)


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully deleted."), 200)


###########################
# nested routes with moon #
###########################

# POST /planets/<planet_id>/moons
@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def create_new_moon_to_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    moon_data = request.get_json()
    # new_moon = Moon.from_dict(moon_data)
    # new_moon["planet"] = planet
    new_moon = Moon(
                    name = moon_data["name"],
                    size = moon_data["size"],
                    description = moon_data["description"],
                    planet_id = planet.id
                    )
    
    db.session.add(new_moon)
    db.session.commit()
    
    message = f"Moon {new_moon.name} created and connect with a {new_moon.planet}."
    return make_response(jsonify(message),201)
    
    
# GET /planets/<planet_id>/moons
@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def get_moons_by_planet_id(planet_id):
    planet = validate_model(Planet, planet_id)
    
    moons_response = []
    for moon in planet.moons:
        moons_response.append(moon.to_dict())
    
    return jsonify(moons_response)