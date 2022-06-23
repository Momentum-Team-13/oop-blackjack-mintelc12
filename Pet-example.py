class Pet():
    def __init__(self, name, species, age, color, gender):
        self.name = name
        self.species = species
        self.age = age
        self.color = color
        self.gender = gender

    def __str__(self):
        return f"Pet name = {self.name}. {self.name} is a {self.color} {self.species} and is {self.age} years old. {self.name} is a {self.gender}."

    def call(self):
        return f"{self.name} come here!"

lily = Pet("Lily", "cat", "13", "turtleshell", "female")
print(lily)
print(lily.call())
