from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        app.config['TESTING'] = True
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    from app.models.planet import Planet
    from app.models.moon import Moon
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.planets_routes import planets_bp
    from .routes.moons_routes import moons_bp
    app.register_blueprint(planets_bp)
    app.register_blueprint(moons_bp)

    return app
