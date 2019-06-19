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
            if smallMeteor == 0:
                meteor_velocity_dy = self.velocity.dy + 1.5
                meteor_velocity_dx = self.velocity.dx + 1.5
            else :
                meteor_velocity_dy = self.velocity.dy - 1.5
                meteor_velocity_dx = self.velocity.dx + 1.5
            
            smallMeteor = SmallMeteor()
            smallMeteor.velocity.dx = meteor_velocity_dx
            smallMeteor.velocity.dy = meteor_velocity_dy
            smallMeteor.center.x = self.center.x
            smallMeteor.center.y = self.center.y
            

            meteorList.append(smallMeteor)
        self.alive = False