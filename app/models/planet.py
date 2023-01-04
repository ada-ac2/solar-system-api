from app import db


class Planet(db.Model):
    
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    gravity = db.Column(db.Float)
    distance_from_earth = db.Column(db.Float)

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["gravity"] = self.gravity
        planet_as_dict["distance_from_earth"] = self.distance_from_earth        

        return planet_as_dict