from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    livable = db.Column(db.Boolean, default = False) 
    number_of_moons = db.Column(db.Integer, nullable = True)
    length_of_year = db.Column(db.Integer, nullable = False)
    namesake = db.Column(db.String, nullable = False)
    atmosphere = db.Column(db.String, nullable = False)
    diameter = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    color = db.Column(db.String,nullable = True)