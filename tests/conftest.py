import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet
from app.models.moon import Moon

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
def one_planet_with_moons(app):
    moon1 = Moon(
        name = "Test1", 
        description = "Fantasy moon for testing purpose.", 
        size = 3.5)
    moon2 = Moon(
        description = "Moon just for testing.",
        size = 17,
        name = "Moon_Test2"
    )
    planet_mercury = Planet(
        name = "Mercury", 
        description = "Mercury is the smallest planet in the Solar System and the closest to the Sun.", 
        length_of_year = 88,
        moons = [moon1, moon2])

    db.session.add(planet_mercury)
    db.session.commit()
    db.session.refresh(planet_mercury, ["id"])
    return planet_mercury

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

@pytest.fixture
def three_planets_with_moons(app):
    moon1 = Moon(
        description = "Moon1 for testing purpose.",
        size = 173.1,
        name = "Moon_Test1")
    moon2 = Moon(
        description = "Moon2 just for testing.",
        size = 17,
        name = "Moon_Test2")
    moon3 = Moon(
        description = "Moon3 for testing purpose.",
        size = 11,
        name = "Moon_Test3")
    moon4 = Moon(
        description = "Moon4 just for testing.",
        size = 19,
        name = "Moon_Test4")

    planet_mercury = Planet(
        name = "Mercury", 
        description = "Mercury is the smallest planet in the Solar System and the closest to the Sun.", 
        length_of_year = 88,
        moons = [moon1, moon2])
    planet_venus = Planet(
        name = "Venus", 
        description = "Venus spins slowly in the opposite direction from most planets.", 
        length_of_year = 225,
        moons = [moon3])
    planet_earth = Planet(
        name = "Earth", 
        description = "Earth — our home planet.", 
        length_of_year = 365,
        moons = [moon4])

    db.session.add_all([planet_mercury, planet_venus, planet_earth])
    db.session.commit()

@pytest.fixture
def one_moon(app):
    moon1 = Moon(
        name = "Test1", 
        description = "Fantasy moon for testing purpose.", 
        size = 3.5)

    db.session.add(moon1)
    db.session.commit()
    db.session.refresh(moon1, ["id"])
    return moon1

@pytest.fixture
def three_moons(app):
    moon1 = Moon(
        name = "Test1", 
        description = "Fantasy moon for testing purpose.", 
        size = 3.5)

    moon2 = Moon(
        name = "Test2", 
        description = "Fantasy moon for testing purpose.", 
        size = 4.0)

    moon3 = Moon(
        name = "Test3", 
        description = "Fantasy moon for testing purpose.", 
        size = 5.5)
    db.session.add_all([moon1, moon2, moon3])
    db.session.commit()
