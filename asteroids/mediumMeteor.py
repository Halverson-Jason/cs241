from meteor import Meteor
from smallMeteor import SmallMeteor
import random

SMALL_METEOR_NUM = 2

RADIUS = 5
ROTATION = -2

RANDOM_LIMIT = 1.5
VELOCITY_CHANGE = 1.5

class MediumMeteor(Meteor):
    def __init__(self,starting_point = None):
        super().__init__(starting_point)
        self.img = "images/meteorGrey_med1.png"
        self.radius = RADIUS # I know this should be 15 but 25 is closer to the radius for a 100px object
        self.rotation = ROTATION
        random.seed()
        x_velocity = random.uniform(-RANDOM_LIMIT,RANDOM_LIMIT)
        y_velocity = random.uniform(-RANDOM_LIMIT,RANDOM_LIMIT)
        self.velocity.dx = x_velocity
        self.velocity.dy = y_velocity

    def split(self,meteorList: list):
        for smallMeteor in range(SMALL_METEOR_NUM):
            if smallMeteor == 0:
                meteor_velocity_dy = self.velocity.dy + VELOCITY_CHANGE
                meteor_velocity_dx = self.velocity.dx + VELOCITY_CHANGE
            else :
                meteor_velocity_dy = self.velocity.dy - VELOCITY_CHANGE
                meteor_velocity_dx = self.velocity.dx + VELOCITY_CHANGE
            
            smallMeteor = SmallMeteor()
            smallMeteor.velocity.dx = meteor_velocity_dx
            smallMeteor.velocity.dy = meteor_velocity_dy
            smallMeteor.center.x = self.center.x
            smallMeteor.center.y = self.center.y
            

            meteorList.append(smallMeteor)
        self.alive = False