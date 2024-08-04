import random
from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        if random.uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
