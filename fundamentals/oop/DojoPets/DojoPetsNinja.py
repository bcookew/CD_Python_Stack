from DojoPetsPet import Dog

class Ninja:
    def __init__(self, firstName, lastName, treats, petFood, pet):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = treats
        self.petFood = petFood
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

steve = Dog("Steve", ["Sit","Fetch"], 100, 100)
ben = Ninja("Ben", "McPherson", True, True, steve)

ben.feed().walk().bathe()