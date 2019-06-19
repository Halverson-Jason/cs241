from meteor import Meteor

import random

RADIUS = 2
ROTATION = 5

RANDOM_LIMIT = 1.5
VELOCITY_CHANGE = 1.5

class SmallMeteor(Meteor):
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_small1.png"
        self.radius = RADIUS # I know this should be 15 but 25 is closer to the radius for a 100px object
        self.rotation = ROTATION
        random.seed()
        x_velocity = random.uniform(-RANDOM_LIMIT,RANDOM_LIMIT)
        y_velocity = random.uniform(-RANDOM_LIMIT,RANDOM_LIMIT)
        self.velocity.dx = x_velocity
        self.velocity.dy = y_velocity

    def split(self,meteorList: list):
        self.alive = False