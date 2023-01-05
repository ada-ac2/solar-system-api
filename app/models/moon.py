from app import db
class Moon(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    #planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False)
    #planet = db.relationship("Planet", back_populates="Moon")

    def to_dict(self):
        moon_as_dict = {}
        moon_as_dict["id"] = self.id
        moon_as_dict["name"] = self.name
        #moon_as_dict["planet_id"] = self.planet_id

        return moon_as_dict

    @classmethod
    def from_dict(cls, moon_data):
        new_moon = Moon(
            name=moon_data["name"],
            description=moon_data["description"],
            orbit_days=moon_data["orbit_days"],
            num_moons=moon_data["num_moons"]
                        )
        return new_moon
