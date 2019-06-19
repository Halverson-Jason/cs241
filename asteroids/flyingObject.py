from point import Point
from velocity import Velocity

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class FlyingObject:
    """The FlyingObject has all the"""
    def __init__(self):
        self.alive = True
        self.velocity = Velocity(0,0)
        self.center = Point()
        self.isWrapX = False
        self.isWrapY = False

    def isAlive(self):
        return self.alive

    #TODO: refactor this, not needed
    def setPoint(self, point: Point):
        self.center = point

    #TODO: refactor this, not needed
    def setVelocity(self,velocity = None, dx = None, dy = None):
        if velocity != None:
            self.velocity = velocity
        elif dx != None and dy != None:
            self.velocity.vector = (dx,dy)

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

    def is_off_screen(self,screen_width,screen_height):
        if self.center.x < 0 or self.center.x > SCREEN_WIDTH or self.center.y < 0 or self.center.y > SCREEN_HEIGHT :
            return True
        else:
            return False