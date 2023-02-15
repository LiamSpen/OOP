import random

# The Coin class simulates a coin that can
# be flipped.


class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):
        # The __ makes it private so you can only alter the value by going through the method.
        self.__sideup = 'Heads'
        # The attributes that we are defining for the class Coin are what goes inside of this init(self)

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    # The above is a mutator method which means that it can change the value of an attribute. Also called a set method.

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
        return self.__sideup
    # This is an accessor method which means that it just returns a value for an attribute.
    # We separate these so that we can just know what the value of the attribute is. IF we put it in the toss then it would change the value before we could find what it equals.
