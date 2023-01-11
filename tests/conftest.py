import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

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
def one_saved_planet(app):
    earth = Planet(
        name="Earth",
        description="Our home planet.",
        orbit_days=365,
        num_moons=1
    )
    db.session.add(earth)
    db.session.commit()
    db.session.refresh(earth, ["id"])
    return earth