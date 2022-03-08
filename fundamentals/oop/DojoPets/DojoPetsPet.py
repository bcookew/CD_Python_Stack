class Pet:
    def __init__(self, name, type, health, energy):
        self.name = name
        self.type = type
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
    
    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5
    
    def noise(self):
        print("pet's sound")

class Dog(Pet):
    def __init__(self, name, tricks, health, energy):
        type = "Dog"
        self.tricks = tricks
        super().__init__(name, type, health, energy)