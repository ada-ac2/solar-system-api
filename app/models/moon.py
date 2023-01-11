from app import db
class Moon(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    size = db.Column(db.Integer())
    description = db.Column(db.String())
    distance_from_planet = db.Column(db.Integer())
    planet_id = db.Column(db.Integer(), db.ForeignKey('planet.id'))
    planet = db.relationship("Planet", back_populates="moons")

    def to_dict(self):
        moon_as_dict = {}
        moon_as_dict["id"] = self.id
        moon_as_dict["name"] = self.name
        moon_as_dict["size"] = self.size
        moon_as_dict["description"] = self.description
        moon_as_dict["distance_from_planet"] = self.distance_from_planet
        moon_as_dict["planet_id"] = self.planet_id
        
        return moon_as_dict

    @classmethod
    def from_dict(cls, moon_data):
        new_moon = Moon(
            name=moon_data["name"],
            description=moon_data["description"],
            size=moon_data["size"],
            distance_from_planet=moon_data["distance_from_planet"],
            planet_id=moon_data["planet_id"]
                        )
        return new_moon
