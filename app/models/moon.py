#get db access
from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates="moons")

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "description": self.description,
    #         "color": self.color
    #     }


    # @classmethod
    # def from_dict(cls, planet_data):
    #     new_planet = Planet(
    #                 name = planet_data["name"],
    #                 description = planet_data["description"],
    #                 color = planet_data["color"]
    #                 )
    #     return new_planet