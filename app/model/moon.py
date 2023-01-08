from app import db
class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    name = db.Column(db.String)
    size = db.Column(db.Float)
    description = db.Column(db.String)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates="moons")
    

    def to_dict(self):
        moon_dict = {}
        moon_dict["id"] = self.id
        moon_dict["name"] = self.name
        
        return moon_dict

    @classmethod
    def from_dict(cls, moon_data):
        new_moon = Moon(name=moon_data["name"])

        return new_moon
