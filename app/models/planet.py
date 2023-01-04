from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
<<<<<<< HEAD
    length_of_year = db.Column(db.Integer, nullable = False)   
    description = db.Column(db.String, nullable = False)
    
=======
    length_of_year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String, nullable = False)
>>>>>>> 1ba96d17c15051edb945c00d33efce0c7b3ba55a
