# polymorphsm with classes

class Bird():
    def sound(self):
        print("Birds make sound")


class Crow(Bird):
    def sound(self):
        print("Crow make Caw Caw sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot makes Squeak sound")

bird1 = Crow()
bird2 = Parrot()

bird1.sound()
bird2.sound()