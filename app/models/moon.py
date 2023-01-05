from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.Integer)
    description = db.Column(db.String)
    name = db.Column(db.String)
    planet_id = db.Column(db.Integer, db.ForeignKey('moon.id'))
    planet = db.relationship("Planet", back_populates = "moons")

    def to_dict(self):
        moon_dict = {}
        moon_dict["id"] = self.id
        moon_dict["size"] = self.size
        moon_dict["description"] = self.description
        moon_dict["name"] = self.name
        return moon_dict

    @classmethod
    def from_dict(cls, moon_data):
        new_moon = Moon(
            name = moon_data["name"],
            description = moon_data["description"],
            size = moon_data["size"]
        )
        return new_moon