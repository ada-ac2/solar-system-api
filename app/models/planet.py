from app import db

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    mass = db.Column(db.Float, nullable=False)
    
    @classmethod
    def get_all_attrs(cls):
        """
        Returns all existing attributes (list) in Planet class
        """
        return [attr for attr in dir(Planet) if not attr.startswith('__')]

    @classmethod
    def from_dict(cls, dict):
        return Planet(name=dict["name"],
            description=dict["description"],
            mass=dict["mass"])
    
    def to_dict(self):
        """
        Returns dictionary containing Planet instance data
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "mass": self.mass
        }