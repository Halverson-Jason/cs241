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

    def setPoint(self, point: Point):
        self.center = point

    def setVelocity(self,velocity = None, dx = None, dy = None):
        if velocity != None:
            self.velocity = velocity
        elif dx != None and dy != None:
            #TODO: Fix to fit properties
            self.velocity.set_dx(dx)
            self.velocity.set_dy(dy)

    def advance(self):
        #TODO: Screen wrap at angles is wierd
        #TODO: Refactor Modifier variable
        modifier = SCREEN_WIDTH/SCREEN_HEIGHT

        if not self.isWrapY and (self.center.center_y >= SCREEN_HEIGHT):
            #This adds advance wraping for top edge.
            #if positive velocity
            if self.velocity.dx > 0:
                if self.center.center_x > SCREEN_HEIGHT:
                    self.center.center_x = SCREEN_WIDTH - self.center.center_x
                    self.center.center_y = 0
                else:
                    if self.center.center_x > (SCREEN_WIDTH/2):
                        self.center.center_x = SCREEN_WIDTH - self.center.center_x
                        self.center.center_y = 0
                    else:
                        self.center.center_y = self.center.center_x
                        self.center.center_x = 0
            #if negative velocity:
            elif self.velocity.dx < 0:
                if self.center.center_x > SCREEN_HEIGHT:
                    self.center.center_y = SCREEN_WIDTH - self.center.center_x
                    self.center.center_x = SCREEN_WIDTH
                else:
                    self.center.center_x = self.center.center_y
                    self.center.center_y = 0
            else:
                self.center.center_y = 0
            self.isWrapY = True

        elif not self.isWrapY and (self.center.center_y <= 0):
            #This adds advance wraping for bottom edge.
            #if positive velocity
            if self.velocity.dx > 0:
                if self.center.center_x > SCREEN_HEIGHT:
                    self.center.center_x = SCREEN_WIDTH - self.center.center_x
                    self.center.center_y = SCREEN_HEIGHT
                else:
                    if self.center.center_x > (SCREEN_WIDTH/2):
                        self.center.center_x = SCREEN_WIDTH - self.center.center_x
                        self.center.center_y = SCREEN_HEIGHT
                    else:
                        self.center.center_y = self.center.center_x
                        self.center.center_x = 0
            #if negative velocity:
            elif self.velocity.dx < 0:
                if self.center.center_x > (SCREEN_WIDTH/2):
                    self.center.center_y = SCREEN_WIDTH - self.center.center_x
                    self.center.center_x = SCREEN_WIDTH
                else:
                    self.center.center_y = SCREEN_HEIGHT
                    self.center.center_x = SCREEN_WIDTH - self.center.center_x
            else:
                self.center.center_y = SCREEN_HEIGHT
            self.isWrapY = True
        # elif not self.isWrapX and (self.center.center_x >= SCREEN_WIDTH):
        #     self.center.center_x = 0
        #     self.isWrapX = True
        #     print("x: {} y: {}".format(self.center.center_x, self.center.center_y))

        # elif not self.isWrapX and (self.center.center_x <= 0):
        #     self.center.center_x = SCREEN_WIDTH
        #     self.isWrapX = True


        else:
            self.isWrapX = False
            self.isWrapY = False

        self.center.add_dx(self.velocity.dx)
        self.center.add_dy(self.velocity.dy)

    def kill(self):
        self.alive = False

    def is_off_screen(self,screen_width,screen_height):
        if self.center.center_x < 0 or self.center.center_x > 600 or self.center.center_y < 0 or self.center.center_y > 500 :
            return True
        else:
            return False