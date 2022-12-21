from app import db
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    atmosphere = db.Column(db.String)
    diameter = db.Column(db.Integer)
    description = db.Column(db.Text)


    # def __init__(self, id , name, atmosphere, diameter,description):
    #     self.id = id
    #     self.name = name
    #     self.atmosphere = atmosphere
    #     self.diameter = diameter
    #     self.description = description

    # def convert_to_dict(self):
    #     return {
    #             "id":self.id,
    #             "name":self.name,
    #             "atmosphere":self.atmosphere,
    #             "diameter":self.diameter,
    #             "description":self.description
    #         }
# planets_list = [
#     Planet(1,"Mercury","minimal","0.383","The smallest planet in our solar system and nearest to the Sun."),
#     Planet(2,"Venus","CO2, N2","0.949","Venus is the second planet from the Sun and is Earth’s closest planetary neighbor."),
#     Planet(3,"Earth","N2, O2, Ar","1.000","Our home planet is the third planet from the Sun."),
#     Planet(4,"Mars","CO2, N2, Ar","0.532","Mars is the fourth planet from the Sun – a dusty, cold, desert world with a very thin atmosphere."),
#     Planet(5,"Jupiter","H2, He","11.209","Jupiter has a long history of surprising scientists."),
#     Planet(6,"Saturn","H2, He","9.449","Saturn is the sixth planet from the Sun and the second-largest planet in our solar system.")   
# ]