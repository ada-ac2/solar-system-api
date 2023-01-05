#get db access
from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    moons = db.relationship("Moon", back_populates="planet")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "color": self.color,
            "moons": [moon.name for moon in self.moons]
        }


    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
                    name = planet_data["name"],
                    description = planet_data["description"],
                    color = planet_data["color"]
                    )
        return new_planet