from flask import Flask



def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.planet import Planet

    from .routes.planet_routes import planets_bp
    app.register_blueprint(planets_bp)

    return app