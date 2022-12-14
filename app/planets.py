class Planet():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [
    Planet(id = 3, name = "Earth", description = "habitable"),
    Planet(id = 1, name = "Mercury", description = "inhabitable"),
    Planet(id = 4, name = "Mars", description = "inhabitable")
]