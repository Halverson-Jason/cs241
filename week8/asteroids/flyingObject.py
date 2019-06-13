from point import Point
from velocity import Velocity

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class FlyingObject:
    """The FlyingObject has all the"""
    def __init__(self,starting_point = Point(200,200)):
        self.alive = True
        self.velocity = Velocity(0,0)
        self.center = starting_point
        self.isWrapX = False
        self.isWrapY = False

    def isAlive(self):
        return self.alive

    def setPoint(self, point):
        self.center = point

    def setVelocity(self,velocity = None, dx = None, dy = None):
        if velocity != None:
            self.velocity = velocity
        elif dx != None and dy != None:
            #TODO: Fix to fit properties
            self.velocity.set_dx(dx)
            self.velocity.set_dy(dy)

    def advance(self):

        if not self.isWrapX and self.center.center_x >= SCREEN_WIDTH:
            #TODO: Fix accessing private variables...
            self.center.x = 0
            self.isWrapX = True
            print(self.center.center_x)

        elif not self.isWrapX and self.center.center_x <= 0:
            self.center.center_x = SCREEN_WIDTH
            self.isWrapX = True

        elif not self.isWrapY and self.center.center_y >= SCREEN_HEIGHT:
            #TODO: Fix accessing private variables...
            self.center.y = 0
            self.isWrapY = True

        elif not self.isWrapY and self.center.center_y <= 0 :
            self.center.center_y = SCREEN_HEIGHT
            self.isWrapY = True

        else:
            self.isWrapX = False
            self.isWrapY = False

        self.center.center_x = self.velocity.dx
        self.center.center_y = self.velocity.dy

    def kill(self):
        self.alive = False

    def is_off_screen(self,screen_width,screen_height):
        if self.center.center_x < 0 or self.center.center_x > 600 or self.center.center_y < 0 or self.center.center_y > 500 :
            return True
        else:
            return False