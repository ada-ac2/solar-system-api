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
def two_saved_planets(app):
    # Arrange
    mars = Planet(name="Mars",
                    description="War planet",
                    radius=2106.1)
    venus = Planet(name="Venus",
                    description="Planet Of Love",
                    radius=3760.4)

    db.session.add_all([mars, venus])
    db.session.commit()