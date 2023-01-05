from app import db
class Planet(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    orbit_days = db.Column(db.Integer())
    num_moons = db.Column(db.Integer())
    moons = db.relationship("Moon", back_populates="planet")

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["orbit_days"] = self.orbit_days
        planet_as_dict["num_moons"] = self.num_moons
        moons_list = []
        for moon in self.moons:
            moons_list.append(moon.to_dict())
        planet_as_dict["moons"] = moons_list

        return planet_as_dict

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
                        name=planet_data["name"],
                        description=planet_data["description"],
                        orbit_days=planet_data["orbit_days"],
                        num_moons=planet_data["num_moons"],
                        
                        )
        return new_planet
