class Planet:
    def __init__(self, id , name, atmosphere, diameter,description):
        self.id = id
        self.name = name
        self.atmosphere = atmosphere
        self.diameter = diameter
        self.description = description

planets_list = [
    Planet("1","Mercury","minimal","0.383","The smallest planet in our solar system and nearest to the Sun, Mercury is only slightly larger than Earth's Moon."),
    Planet("2","Venus","CO2, N2","0.949","Venus is the second planet from the Sun and is Earth’s closest planetary neighbor. It’s one of the four inner, terrestrial (or rocky) planets, and it’s often called Earth’s twin because it’s similar in size and density. These are not identical twins, however – there are radical differences between the two worlds."),
    Planet("3","Earth","N2, O2, Ar","1.000","Our home planet is the third planet from the Sun, and the only place we know of so far that’s inhabited by living things."),
    Planet("4","Mars","CO2, N2, Ar","0.532","Mars is the fourth planet from the Sun – a dusty, cold, desert world with a very thin atmosphere. Mars is also a dynamic planet with seasons, polar ice caps, canyons, extinct volcanoes, and evidence that it was even more active in the past."),
    Planet("5","Jupiter","H2, He","11.209","Jupiter has a long history of surprising scientists – all the way back to 1610 when Galileo Galilei found the first moons beyond Earth. That discovery changed the way we see the universe."),
    Planet("6","Saturn","H2, He","9.449","Saturn is the sixth planet from the Sun and the second-largest planet in our solar system.")   
]