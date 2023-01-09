from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    radius = db.Column(db.Float)
    num_moons = db.Column(db.Float)
    gravity = db.Column(db.Float)
    moons = db.relationship("Moon", back_populates="planet")

    def to_dict(self):
        planet_dict = {}
        planet_dict["id"] = self.id
        planet_dict["name"] = self.name
        planet_dict["description"] = self.description
        planet_dict["radius"] = self.radius
        planet_dict["num_moons"] = self.num_moons
        planet_dict["gravity"] = self.gravity

        moon_names = []
        for moon in self.moons:
            moon_names.append(moon.name)
        planet_dict["moon"] = moon_names
        return planet_dict

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                    description=planet_data["description"],
                    radius=planet_data["radius"],
                    num_moons=planet_data["num_moons"],
                    gravity=planet_data["gravity"]
                    )
        return new_planet

