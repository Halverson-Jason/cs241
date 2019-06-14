from meteor import Meteor
import random

class LargeMeteor(Meteor):
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_big1.png"
        self.radius = 25
        self.rotation = 1
        random.seed()
        x_velocity = random.uniform(-1.5,1.5)
        y_velocity = random.uniform(-1.5,1.5)
        self.velocity.dx = x_velocity
        self.velocity.dy = y_velocity

    def split(self):
        self.alive = False