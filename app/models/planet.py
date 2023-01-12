from app import db

# planets = [Planet(1, "Neptune", "thick, windy", 1.024e26 ),
#            Planet(2, "Mars", "dusty, cold desert",6.39e23),
#            Planet(3, "Earth", "rocky, terrestrial, full of life",5.972e24)
#            ]

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    mass = db.Column(db.Float, nullable=False)
    # gravity = db.Column(db.Float, nullable=False)
    # dist_sun = db.Column(db.Float, nullable=False)
    # n_moons = db.Column(db.Integer, nullable=False)
    # water
    # temperature
    # atmosphere
    
    def get_all_attrs():
        """
        Returns all existing attributes (list) in Planet class
        """
        return [attr for attr in dir(Planet) if not attr.startswith('__')]