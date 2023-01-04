from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
from sqlalchemy import desc, asc


# ---------helper functions--------
def sort_planet_query(planet_query, sort_query, order_query):
    if not sort_query:
        sort_query = "name"

    if not order_query:
        order_query = "asc"

    if order_query == "desc":
        planet_query = planet_query.order_by(desc(sort_query))
    else:
        planet_query = planet_query.order_by(asc(sort_query))

    return planet_query



def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet #{planet_id} is not an int."}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"Planet #{planet_id} not found"}, 404))
    
    return planet


# ------------route implementations-----------
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body or 'diameter_in_km' not in request_body:
        return make_response("Invalid Request", 400)

    new_planet = Planet(name = request_body["name"], 
                        description = request_body["description"], 
                        diameter_in_km = request_body["diameter_in_km"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("", methods=["GET"])
def get_planets_optional_query():
    planet_query = Planet.query
    name_query = request.args.get("name")

    if name_query:
        planet_query = planet_query.filter(Planet.name.ilike(f"%{name_query}%"))

    sort_query = request.args.get("sort")
    order_query = request.args.get("order")

    if sort_query or order_query:
        planet_query = sort_planet_query(planet_query, sort_query, order_query)

    planets = planet_query.all()
    planets_response = []

    for planet in planets:
        planets_response.append(planet.to_dict())

    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet_by_id(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict()


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter_in_km = request_body["diameter_in_km"]

    db.session.commit()
    return make_response(f"Planet #{planet_id} successfully updated.")


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet #{planet_id} successfully deleted")


# --------------for testing-----------------
# planets = [
#     Planet(id = 3, name = "Earth", description = "habitable", diameter = 12756),
#     Planet(id = 1, name = "Mercury", description = "inhabitable", diameter = 4879),
#     Planet(id = 4, name = "Mars", description = "inhabitable", diameter = 6792)
# 