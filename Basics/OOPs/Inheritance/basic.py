class Animal:
    def speak(self):
        print("Animal makes sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


sheru = Dog()
sheru.speak()
sheru.bark()