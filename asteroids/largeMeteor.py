from meteor import Meteor
from mediumMeteor import MediumMeteor
from smallMeteor import SmallMeteor
import random

RADIUS = 25

RANDOM_LIMIT = 1.5
RANDOM_START = -300
RANDOM_END = 300

MEDIUM_METEOR_NUM = 2

MEDIUM_VELOCITY_CHANGE = 2
SMALL_VELOCITY_CHANGE = 5

class LargeMeteor(Meteor):
    def __init__(self):
        starting_point = self.get_random_point(RANDOM_START,RANDOM_END)
        super().__init__(starting_point)
        self.img = "images/meteorGrey_big1.png"
        self.radius = RADIUS # I know this should be 15 but 25 is closer to the radius for a 100px object
        self.rotation = 1
        self.velocity = self.get_random_velocity(-RANDOM_LIMIT,RANDOM_LIMIT)

    def split(self,meteorList: list):
        for mediumMeteor in range(MEDIUM_METEOR_NUM):

            if mediumMeteor == 0:
                dy = self.velocity.dy + MEDIUM_VELOCITY_CHANGE
            else:
                dy = self.velocity.dy - MEDIUM_VELOCITY_CHANGE

            dx = self.velocity.dx
            mediumMeteor = MediumMeteor(self.center)
            mediumMeteor.velocity.vector = (dx,dy)
            meteorList.append(mediumMeteor)

        smallMeteor = SmallMeteor(self.center)
        smallMeteor.velocity.dx = self.velocity.dx + SMALL_VELOCITY_CHANGE

        meteorList.append(smallMeteor)
        self.alive = False