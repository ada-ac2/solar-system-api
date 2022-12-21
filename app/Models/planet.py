from app import db


class Planets(db.Model):
    
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    gravity = db.Column(db.String)
    distance = db.Column(db.String)
    