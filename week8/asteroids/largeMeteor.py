from meteor import Meteor
from mediumMeteor import MediumMeteor
from smallMeteor import SmallMeteor
import random

class LargeMeteor(Meteor):
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_big1.png"
        self.radius = 25 # I know this should be 15 but 25 is closer to the radius for a 100px object
        self.rotation = 1
        random.seed()
        x_velocity = random.uniform(-1.5,1.5)
        y_velocity = random.uniform(-1.5,1.5)
        self.velocity.dx = x_velocity
        self.velocity.dy = y_velocity

    def split(self,meteorList: list):
        for mediumMeteor in range(2):
            mediumMeteor = MediumMeteor()
            mediumMeteor.center.center_x = self.center.center_x
            mediumMeteor.center.center_y = self.center.center_y
            meteorList.append(mediumMeteor)
        smallMeteor = SmallMeteor()
        smallMeteor.center.center_x = self.center.center_x
        smallMeteor.center.center_y = self.center.center_y
        meteorList.append(smallMeteor)
        self.alive = False