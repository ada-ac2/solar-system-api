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

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
            name = planet_data["name"],
            description = planet_data["description"],
            diameter_in_km = planet_data["diameter_in_km"]
        )
        return new_planet