from app import db
from app.models.moon import Moon
from flask import Blueprint, jsonify, abort, make_response, request
from .planet_routes import validate_model

moons_bp = Blueprint("moons_bp", __name__, url_prefix = "/moons")