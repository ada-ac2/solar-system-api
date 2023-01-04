from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    radius = db.Column(db.Float)
    num_moons = db.Column(db.Float)
    gravity = db.Column(db.Float)

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "radius": self.radius,
                "num_moons": self.num_moons,
                "gravity": self.gravity 
            }


