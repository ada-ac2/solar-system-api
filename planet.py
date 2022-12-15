class Planet:
    def __init__(self, id, name, description, len_years, num_moons):
        self.id = id
        self.name = name
        self.description = description
        self.len_years = len_years
        self.num_moons = num_moons
        

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "length of year": self.len_years,
            "number of moons": self.num_moons,
        }