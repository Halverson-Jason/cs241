from point import Point
from velocity import Velocity

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class FlyingObject:
    """The FlyingObject has all the"""
    def __init__(self,center=None):
        self.alive = True
        self.velocity = Velocity()
        self.isWrapX = False
        self.isWrapY = False

        if center == None:
            self.center = Point()
        else:
            self.center = center.copy()

    def advance(self):

        if self.center.x >= SCREEN_WIDTH:
            self.center.x = 0

        elif self.center.x <= 0:
            self.center.x = SCREEN_WIDTH

        if self.center.y >= SCREEN_HEIGHT:
            self.center.y = 0

        elif self.center.y <= 0 :
            self.center.y = SCREEN_HEIGHT

        self.center.add_dx(self.velocity.dx)
        self.center.add_dy(self.velocity.dy)

    def kill(self):
        self.alive = False