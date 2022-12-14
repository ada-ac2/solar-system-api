from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, num_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_moons = num_moons

    planets = [
        Planet(1, "Mercury", "Mercury is the closest planet to the Sun", 0),
        Planet(2, "Venus", "Venus is the hottest planet in the solar system", 0 ),
        Planet(3, "Earth", "Our home planet", 1)
    ]