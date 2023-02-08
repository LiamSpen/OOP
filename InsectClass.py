import random


class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.miles = 0

    def flight(self):
        self.miles = random.randint(1, 10)

    def get_flight(self):
        return self.miles
