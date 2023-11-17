from random import *
class die:
    def __init__(self, slides):
        self.slides = slides
    def roll_die(self):
        print(randint(1, self.slides))
roll = die(6)
for i in range(10):
    roll.roll_die()
