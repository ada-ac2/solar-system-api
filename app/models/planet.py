from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    length_of_year = db.Column(db.Integer, nullable = False)   
    description = db.Column(db.String, nullable = False)
    moons = db.relationship("Moon", back_populates="planets")

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["length_of_year"] = self.length_of_year
        planet_as_dict["description"] = self.description
        return planet_as_dict


    @classmethod
    def from_dict(cls,planet_data):
        new_planet = Planet(name=planet_data["name"],
                        length_of_year=planet_data["length_of_year"],
                        description=planet_data["description"])
        return new_planet