from app import db
from flask import Blueprint, jsonify, abort, make_response, request 
from app.model.planet import Planet
from app.model.moon import Moon

planets_bp = Blueprint("planets_bp",__name__, url_prefix="/planets")
moons_bp = Blueprint("moons_bp",__name__, url_prefix="/moons")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
    
    return model
#============================== planets_bp.route =============================
#============================================================================
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

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


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.radius = request_body["radius"]

    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")
#============================== "/<planet_id>/moons" =============================
#============================================================================

@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def add_new_moon_to_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)
    new_moon.planet = planet

    db.session.add(new_moon)
    db.session.commit()

    message = f"Moon {new_moon.name} created with Planet {planet.name}"
    return make_response(jsonify(message), 201)

@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def get_all_moons_for_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    moons_response = []
    for moon in planet.moons:
        moons_response.append(moon.to_dict())

    return jsonify(moons_response)

#============================== moons_bp.route =============================
#============================================================================


@moons_bp.route("", methods=["POST"])
def create_moon():
    moon_data = request.get_json()
    new_moon = Moon.from_dict(moon_data)

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"Moon {new_moon.name} created", 201)

@moons_bp.route("", methods=["GET"])
def read_all_moons():
    moons = Moon.query.all()
    moons_response = []
    for moon in moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response)

@moons_bp.route("<moon_id>", methods=["GET"])
def read_one_moon(moon_id):
   moon = validate_model(Moon, moon_id)
   return moon.to_dict()

@moons_bp.route("<moon_id>", methods=["DELETE"])
def delete_one_moon(moon_id):
    moon = validate_model(Moon, moon_id)

    db.session.delete(moon)
    db.session.commit()

    return make_response(f"Moon #{moon.id} successfully deleted")

@moons_bp.route("<moon_id>", methods=["PUT"])
def update_moon(moon_id):
    moon = validate_model(Moon, moon_id)

    request_body = request.get_json()

    moon.name = request_body["name"]
    moon.description = request_body["description"]
    moon.size = request_body["size"]

    db.session.commit()
    return make_response(f"Moon #{moon.id} successfully updated")