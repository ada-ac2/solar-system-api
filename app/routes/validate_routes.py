from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from flask import Blueprint, jsonify, abort, make_response, request

# Validating the id of the instance: id needs to be int and exists the instance with the id.
# Returning the valid Class instance if valid id
# Work for Planet and Moon classes
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response(jsonify(f"{cls.__name__} {model_id} invalid"), 400))
    class_obj = cls.query.get(model_id)
    if not class_obj:
        abort(make_response(jsonify(f"{cls.__name__} {model_id} not found"), 404))
    return class_obj

# Validating the user input to create or update the table planet
# Returning the valid JSON if valid input
def validate_planet_user_input(planet_value):
    if "name" not in planet_value \
        or not isinstance(planet_value["name"], str) \
        or planet_value["name"] == "" \
        or "length_of_year" not in planet_value \
        or not isinstance(planet_value["length_of_year"], int) \
        or planet_value["length_of_year"] <=0 \
        or "description" not in planet_value \
        or not isinstance(planet_value["description"], str) \
        or planet_value["description"] == "":
        return abort(make_response(jsonify("Invalid request"), 400))  
    return planet_value

# Validating the user input to create or update the table moon
# Returning the valid JSON if valid input
def validate_moon_user_input(moon_value):
    
    #if not "planet_id": moon_value["planet_id"] = 0   ####

    if "name" not in moon_value \
        or not isinstance(moon_value["name"], str) \
        or moon_value["name"] == "" \
        or "size" not in moon_value \
        or not (isinstance(moon_value["size"], float) or isinstance(moon_value["size"], int)) \
        or moon_value["size"] <=0 \
        or "description" not in moon_value \
        or not isinstance(moon_value["description"], str) \
        or moon_value["description"] == "":
            return abort(make_response(jsonify("Invalid request"), 400))  
    return moon_value