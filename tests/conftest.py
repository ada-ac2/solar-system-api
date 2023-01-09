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
def two_saved_planets(app):
    earth = Planet(name="Earth", \
            description="rocky, terrestrial, full of life", mass=5.972e24)
    mars = Planet(name="Mars", description="dusty, cold desert", \
            mass=6.39e23)
    planets = [earth, mars]
    db.session.add_all(planets)
    db.session.commit()

    for planet in planets:
        db.session.refresh(planet, ["id"])

    return planets