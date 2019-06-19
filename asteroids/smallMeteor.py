from meteor import Meteor

import random

class SmallMeteor(Meteor):
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_small1.png"
        self.radius = 2 # I know this should be 15 but 25 is closer to the radius for a 100px object
        self.rotation = 5
        random.seed()
        x_velocity = random.uniform(-1.5,1.5)
        y_velocity = random.uniform(-1.5,1.5)
        self.velocity.dx = x_velocity
        self.velocity.dy = y_velocity

    def split(self,meteorList: list):
        self.alive = False