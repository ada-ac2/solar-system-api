import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.model.planet import Planet
from app.model.moon import Moon


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
def two_planets(app):
    # Arrange
    earth = Planet(name="Earth",
                    description="Our planet",
                    radius=3.95)
    mars = Planet(name="Mars",
                    description="A dust,cold,desert world",
                    radius=2.10)

    db.session.add_all([earth, mars])
    db.session.commit()


@pytest.fixture
def two_moons(app):
    # Arrange
    moon1 = Moon(name="moon1",
                    description="moon1 is small",
                    size=2.4)
    moon2 = Moon(name="moon2",
                    description="moon2 is large",
                    size=3.1)

    db.session.add_all([moon1, moon2])
    db.session.commit()