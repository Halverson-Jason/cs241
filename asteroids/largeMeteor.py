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

            if mediumMeteor == 0:
                mediumMeteor_velocity_dy = self.velocity.dy +2

            else:
                mediumMeteor_velocity_dy = self.velocity.dy -2

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
        smallMeteor.velocity.dx = self.velocity.dx + 5
        meteorList.append(smallMeteor)
        self.alive = False