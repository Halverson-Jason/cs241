from meteor import Meteor

import random

RADIUS = 5
ROTATION = 5

RANDOM_LIMIT = 1.5
VELOCITY_CHANGE = 1.5

class SmallMeteor(Meteor):
    def __init__(self,starting_point = None):
        super().__init__(starting_point)
        self.img = "images/meteorGrey_small1.png"
        self.radius = RADIUS # I know this should be 2 but 5 is closer to the radius for a 25px object
        self.rotation = ROTATION

    def split(self,meteorList: list):
        self.alive = False