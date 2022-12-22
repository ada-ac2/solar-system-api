from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    planet_data = request.get_json()

    new_planet = Planet(
        name = planet_data["name"], 
        description = planet_data["description"], 
        color = planet_data["color"]
    )

    #add new planet to db
    db.session.add(new_planet)
    #commit new planet to db
    db.session.commit()

    return make_response(f"Planet {new_planet.name} created", 201)


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
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        })

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

    return jsonify(planets_response)

def validate_id_return_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet_id {planet_id} invalid."},400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"planet_id {planet_id} not found."},404))
        
    return planet


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_id_return_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated.", 200)


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet_by_id(planet_id):
    planet = validate_id_return_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "color": planet.color
    }


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_id_return_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted.", 200)