import random


class Insect:
    def __init__(self, n, w, l):
        self.name = n
        self.wings = w
        self.legs = l
        self.miles = 0

    def flight(self):
        self.miles = random.randint(1, 10)

    def get_flight(self):
        return self.miles

    def get_name(self):
        return self.name
