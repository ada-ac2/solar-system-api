from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    diameter_in_km = db.Column(db.Integer)

    def to_dict(self):
        return   {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "diameter_in_km": self.diameter_in_km
        }

        