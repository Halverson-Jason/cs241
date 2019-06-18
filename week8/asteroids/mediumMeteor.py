from meteor import Meteor
from smallMeteor import SmallMeteor
import random

class MediumMeteor(Meteor):
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_med1.png"
        self.radius = 5 # I know this should be 15 but 25 is closer to the radius for a 100px object
        self.rotation = -2
        random.seed()
        x_velocity = random.uniform(-1.5,1.5)
        y_velocity = random.uniform(-1.5,1.5)
        self.velocity.dx = x_velocity
        self.velocity.dy = y_velocity

    def split(self,meteorList: list):
        for smallMeteor in range(2):
            smallMeteor = SmallMeteor()
            smallMeteor.center.center_x = self.center.center_x
            smallMeteor.center.center_y = self.center.center_y
            meteorList.append(smallMeteor)
        self.alive = False