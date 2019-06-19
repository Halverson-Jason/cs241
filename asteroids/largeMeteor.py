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
        dx = random.uniform(-RANDOM_LIMIT,RANDOM_LIMIT)
        dy = random.uniform(-RANDOM_LIMIT,RANDOM_LIMIT)
        self.velocity.dx = dx
        self.velocity.dy = dy

    def split(self,meteorList: list):
        for mediumMeteor in range(MEDIUM_METEOR_NUM):

            if mediumMeteor == 0:
                dy = self.velocity.dy + MEDIUM_VELOCITY_CHANGE

            else:
                dy = self.velocity.dy - MEDIUM_VELOCITY_CHANGE

            dx = self.velocity.dx
            mediumMeteor = MediumMeteor()
            mediumMeteor.velocity.set = (dx,dy)

            mediumMeteor.center.coordinate = (self.center.x,self.center.y)

            meteorList.append(mediumMeteor)


        smallMeteor = SmallMeteor()
        smallMeteor.center.coordinate = (self.center.x,self.center.y)
        smallMeteor.velocity.dx = self.velocity.dx + SMALL_VELOCITY_CHANGE
    
        meteorList.append(smallMeteor)
        self.alive = False