from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request 


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    radius=request_body["radius"],
                    num_moons=request_body["num_moons"],
                    gravity=request_body["gravity"]
                    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planet_query = Planet.query
    name_query = request.args.get("name")
    if name_query:
        planet_query = planet_query.filter(Planet.name.ilike(f"%{name_query}%"))
        
    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            planet_query = planet_query.order_by(Planet.name.desc())
        else:
            planet_query = planet_query.order_by(Planet.name.asc())

    planets = planet_query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    
    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    
    return planet

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_book(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.radius = request_body["radius"]
    planet.num_moons = request_body["num_moons"]
    planet.gravity = request_body["gravity"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_book(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")


# @planets_bp.route("/<planet_id>/greater_gravity", methods=["GET"])    
# def find_planets_with_greater_gravity(planet_id):
#     planets_with_greater_gravity = []
#     planet = validate_planet(planet_id)
#     # retrieve that planets gravity value
#     current_planet_gravity = planet.gravity
#     for planet in planets:
#         if planet.gravity > current_planet_gravity:
#             planets_with_greater_gravity.append(planet.to_dict())
#     return jsonify(planets_with_greater_gravity)

# @planets_bp.route("/<planet_id>/greater_radius", methods=["GET"])    
# def find_planets_with_greater_radius(planet_id):
#     planets_with_greater_radius = []
#     planet = validate_planet(planet_id)
#     # retrieve that planets gravity value
#     current_planet_radius = planet.radius
#     for planet in planets:
#         if planet.radius > current_planet_radius:
#             planets_with_greater_radius.append(planet.to_dict())
#     return jsonify(planets_with_greater_radius)



