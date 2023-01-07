from app import db
from app.model.planet import Planet
from flask import Blueprint

planets_bp = Blueprint("planets_bp",__name__, url_prefix="/planets")


