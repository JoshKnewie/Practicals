from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability < random.randint(0, 100):
            super().drive(0)
        else:
            distance_driven = super().drive(distance)
            return distance_driven
