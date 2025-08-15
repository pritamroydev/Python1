from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def start(self):
        pass        # no implementation


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")


veh1 = Bike()
veh2 = Car()

veh1.start()
veh2.start()