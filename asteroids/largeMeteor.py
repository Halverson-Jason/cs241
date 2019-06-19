from meteor import Meteor
from mediumMeteor import MediumMeteor
from smallMeteor import SmallMeteor
import random

RADIUS = 25

RANDOM_LIMIT = 1.5

MEDIUM_METEOR_NUM = 2

MEDIUM_VELOCITY_CHANGE = 2
SMALL_VELOCITY_CHANGE = 5

class LargeMeteor(Meteor):
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_big1.png"
        self.radius = RADIUS # I know this should be 15 but 25 is closer to the radius for a 100px object
        self.rotation = 1
        random.seed()
        x_velocity = random.uniform(-RANDOM_LIMIT,RANDOM_LIMIT)
        y_velocity = random.uniform(-RANDOM_LIMIT,RANDOM_LIMIT)
        self.velocity.dx = x_velocity
        self.velocity.dy = y_velocity

    def split(self,meteorList: list):
        for mediumMeteor in range(MEDIUM_METEOR_NUM):

            if mediumMeteor == 0:
                mediumMeteor_velocity_dy = self.velocity.dy + MEDIUM_VELOCITY_CHANGE


            else:
                mediumMeteor_velocity_dy = self.velocity.dy - MEDIUM_VELOCITY_CHANGE


            mediumMeteor_velocity_dx = self.velocity.dx
            mediumMeteor = MediumMeteor()
            mediumMeteor.velocity.dx = mediumMeteor_velocity_dx
            mediumMeteor.velocity.dy = mediumMeteor_velocity_dy
            mediumMeteor.center.x = self.center.x
            mediumMeteor.center.y = self.center.y
            meteorList.append(mediumMeteor)


        smallMeteor = SmallMeteor()
        smallMeteor.center.x = self.center.x
        smallMeteor.center.y = self.center.y
        smallMeteor.velocity.dx = self.velocity.dx + SMALL_VELOCITY_CHANGE
    
        meteorList.append(smallMeteor)
        self.alive = False