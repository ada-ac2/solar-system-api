from app import db
class Planet(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    orbit_days = db.Column(db.Integer())
    num_moons = db.Column(db.Integer())