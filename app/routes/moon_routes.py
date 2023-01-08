from app import db
from app.models.moon import Moon
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
from .validate_routes import validate_model, validate_moon_user_input, validate_planet_user_input

moons_bp = Blueprint("moons_bp", __name__, url_prefix = "/moons")

# Get all moons info 
# /moons
# Return JSON list
@moons_bp.route("", methods = ["GET"])
def get_all_moons_query():
    moon_query = Moon.query
    # Filtering by moon name (return all records which name contains planet_name_query)
    moon_name_query = request.args.get("name")
    
    if moon_name_query:
        moon_query = moon_query.filter(Moon.name.ilike(f"%{moon_name_query}%"))
    
    # Sorting by moon name
    sort_by_name_query = request.args.get("sort_by_name")
    
    if sort_by_name_query == "desc":
        moon_query = moon_query.order_by(Moon.name.desc()).all()
    elif sort_by_name_query == "asc":
        moon_query = moon_query.order_by(Moon.name).all() 
        
    # Sorting by moon size
    moon_sort_size_query = request.args.get("sort_by_size")
    
    if moon_sort_size_query == "desc":
        moon_query = moon_query.order_by(Moon.size.desc()).all()
    elif sort_by_name_query == "asc":
        moon_query = moon_query.order_by(Moon.size).all()

    # Build response
    moon_response = []
    for moon in moon_query:
        moon_response.append(moon.to_dict())

    return jsonify(moon_response), 200

# Read one moon
# Return one moon info in JSON format    
@moons_bp.route("/<moon_id>",methods=["GET"] )
def get_one_moon(moon_id):
    moon = validate_model(Moon, moon_id)
    return moon.to_dict()

# Create one moon
@moons_bp.route("", methods = ["POST"])
def create_moon():
    moon_value = validate_moon_user_input(request.get_json())
    new_moon = Moon.from_dict(moon_value)

    db.session.add(new_moon)
    db.session.commit()
    return make_response(jsonify(f"Moon {new_moon.name} successfully created"), 201)    

# Delete moon by id
@moons_bp.route("/<moon_id>",methods=["DELETE"])
def delete_moon(moon_id):
    moon = validate_model(Moon, moon_id)
    
    db.session.delete(moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {moon.id} successfully deleted"), 200)