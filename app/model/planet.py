from app import db
class Planet():
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    name = db.Column(db.String)
    description = db.Column(db.String)
    radius = db.Column(db.Float)

    def to_dict(self):
        planet_dict = {}
        planet_dict["id"] = self.id
        planet_dict["name"] = self.name
        planet_dict["description"] = self.name
        planet_dict["radius"] = self.name
        return planet_dict

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                    description=planet_data["description"],
                    radius=planet_data["radius"]

        return new_planet
