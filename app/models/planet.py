from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    diameter_in_km = db.Column(db.Integer)
    moons = db.relationship("Moon", back_populates = "planets")
    

    def to_dict(self):
        planet_dict = {}
        planet_dict["id"] = self.id
        planet_dict["name"] = self.name
        planet_dict["description"] = self.description
        planet_dict["diameter_in_km"] = self.diameter_in_km
        moon_names = []
        for moon in self.moons:
            moon_names.append(moon.name)
        planet_dict["moons"] = moon_names
        return planet_dict


    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
            name = planet_data["name"],
            description = planet_data["description"],
            diameter_in_km = planet_data["diameter_in_km"]
        )
        return new_planet
