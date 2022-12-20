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



#@planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     planets_response = []
#     for planet in list_planets:
#         planets_response.append(planet.convert_planet_to_dict())

#     return jsonify(planets_response)


# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet_by_id(planet_id):
#     planet = validate_id_return_planet(planet_id)
#     return planet.convert_planet_to_dict()


#     def validate_id_return_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"planet_id {planet_id} invalid."},400))

#     for planet in list_planets:
#         if planet.id == planet_id:
#             return planet