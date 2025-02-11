from random import randint

class Die:

    def __init__(self, num_sides=6):
        #six sided die
        self.num_sides=num_sides

    def roll(self):
        #Returns a rendom value between 1 and sides
        return randint(1, self.num_sides)