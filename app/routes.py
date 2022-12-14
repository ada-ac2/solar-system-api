from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

list_planets = [
    Planet(1, "Mercury", "is the smallest planet in the Solar System", "gray"),
    Planet(3, "Earth", "The planet that we live on.", "blue")
]