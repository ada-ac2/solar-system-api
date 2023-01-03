import pytest
from app import create_app, db
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
def two_planets(app):
    earth = Planet(
        name = "Earth", 
        description = "habitable", 
        diameter_in_km = 12756
    )

    mars = Planet(
        name = "Mars", 
        description = "inhabitable", 
        diameter_in_km = 6792
    )

    db.session.add_all([earth, mars])
    db.session.commit()
    db.session.refresh(earth, ["id"])
    db.session.refresh(mars, ["id"])
    #return planet