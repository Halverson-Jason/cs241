from point import Point
from velocity import Velocity

class FlyingObject:
    """The FlyingObject has all the"""
    def __init__(self,starting_point):
        self.alive = True
        self.velocity = Velocity(0,0)
        self.center = starting_point

    def isAlive(self):
        return self.alive

    def setPoint(self, point):
        self.center = point

    def setVelocity(self,velocity = None, dx = None, dy = None):
        if velocity != None:
            self.velocity = velocity
        elif dx != None and dy != None:
            self.velocity.set_dx(dx)
            self.velocity.set_dy(dy)

    def advance(self):
        self.center.add_x(self.velocity.dx)
        self.center.add_y(self.velocity.dy)

    def kill(self):
        self.alive = False

    def is_off_screen(self,screen_width,screen_height):
        if self.center.x < 0 or self.center.x > 600 or self.center.y < 0 or self.center.y > 500 :
            return True
        else:
            return False
