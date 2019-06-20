from meteor import Meteor
from smallMeteor import SmallMeteor
import random

SMALL_METEOR_NUM = 2

RADIUS = 10
ROTATION = -2

RANDOM_LIMIT = 1.5
VELOCITY_CHANGE = 1.5

class MediumMeteor(Meteor):
    def __init__(self,starting_point = None):
        super().__init__(starting_point)
        self.img = "images/meteorGrey_med1.png"
        self.radius = RADIUS # I know this should be 5 but 10 is closer to the radius for a 50px object
        self.rotation = ROTATION

    def split(self,meteorList: list):
        for smallMeteor in range(SMALL_METEOR_NUM):
            if smallMeteor == 0:
                dy = self.velocity.dy + VELOCITY_CHANGE
                dx = self.velocity.dx + VELOCITY_CHANGE
            else :
                dy = self.velocity.dy - VELOCITY_CHANGE
                dx = self.velocity.dx + VELOCITY_CHANGE

            smallMeteor = SmallMeteor(self.center)
            smallMeteor.velocity.vector = (dx,dy)

            meteorList.append(smallMeteor)
        self.alive = False