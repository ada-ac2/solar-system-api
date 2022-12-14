class Planet:
    def __init__(self, id, name, description, radius, num_moons = None, gravity=0):
        self.id = id
        self.name = name
        self.description = description
        self.radius = radius
        self.num_moons = num_moons
        self.gravity = gravity
planets = [
    Planet(1, "Earth","Has human life", 3958.8, 1, 9.08),
    Planet(2, "Mercury","Slate Gray", 1516, 0, 3.7),
    Planet(3, "Venus","Planet of Love", 3760.4, 1, 8.874),
    Planet(4, "Mars","War planet", 2106.1, 2, 3.721),
    Planet(5, "Jupiter","planet of luck", 43441, 80, 24.79),
    Planet(6, "Uranus","Hashumanlife", 15759, 27, 8.87),
    Planet(7, "Saturn","planet of lessons", 36184, 83, 10.44)
]
