from app import db
class Planet(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    orbit_days = db.Column(db.Integer())
    num_moons = db.Column(db.Integer())






# ------------Hardcoded Data for Planet------------------------------
# class Planet:
#     def __init__(self, id, name, description, len_years, num_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.len_years = len_years
#         self.num_moons = num_moons
        

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "length of year": self.len_years,
#             "number of moons": self.num_moons,
#         }