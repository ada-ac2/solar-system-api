import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app(test_config=True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def one_planet(app):
    planet = Planet(
        name = "Mercury", 
        description = "Mercury is the smallest planet in the Solar System and the closest to the Sun.", 
        length_of_year = 88)

    db.session.add(planet)
    db.session.commit()
    db.session.refresh(planet, ["id"])
    return planet

@pytest.fixture
def three_planets(app):
    planet_mercury = Planet(
        name = "Mercury", 
        description = "Mercury is the smallest planet in the Solar System and the closest to the Sun.", 
        length_of_year = 88)
    planet_venus = Planet(
        name = "Venus", 
        description = "Venus spins slowly in the opposite direction from most planets.", 
        length_of_year = 225)
    planet_earth = Planet(
        name = "Earth", 
        description = "Earth — our home planet.", 
        length_of_year = 365)

    db.session.add_all([planet_mercury, planet_venus, planet_earth])
    db.session.commit()