from app import db

class Moon(db.Model):
    __tablename__ = 'moons'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    size = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    discovery_date = db.Column(db.DateTime, nullable=False)
    planet = db.relationship("Planet", back_populates="moons")
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))

    @classmethod
    def get_all_attrs(cls):
        """
        Returns all existing attributes (list) in Planet class
        """
        return [attr for attr in dir(cls) if callable(attr)]

    @classmethod
    def from_dict(cls, dict, planet, planet_id):
        return Moon(
            name=dict["name"],
            size=dict["size"],
            description=dict["description"],
            discovery_date=dict["discovery_date"],
            planet=planet,
            planet_id=planet_id,
            )

    def to_dict(self):
        """
        Returns dictionary containing Planet instance data
        """
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "description": self.description,
            "discovery_date": self.discovery_date,
            "planet_id": self.planet_id,
            #"planet": self.planet.name,
        }
    