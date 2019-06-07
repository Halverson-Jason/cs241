from point import Point
from velocity import Velocity
#TODO: add is_off_screen method
class FlyingObject:

    def __init__(self,starting_point):
        self.alive = True
        self.starting_point = starting_point
        self.velocity = Velocity(0,0)
        self.center = starting_point

    def isAlive(self):
        return self.alive

    def setPoint(self, point):
        self.center = point

    def getPoint(self):
        return self.center

    def setVelocity(self,velocity = None, dx = None, dy = None):
        if velocity != None:
            self.velocity = velocity
        elif dx != None and dy != None:
            self.velocity.set_dx(dx)
            self.velocity.set_dy(dy)

    def getVelocity(self):
        return self.velocity

    def advance(self):
        self.center.add_x(self.velocity.get_dx())
        self.center.add_y(self.velocity.get_dy())

    def kill(self):
        self.alive = False

    def is_off_screen(self,screen_width,screen_height):
        if self.center.get_center_x() < 0 or self.center.get_center_x() > 600 or self.center.get_center_y() < 0 or self.center.get_center_y() > 500 :
            return True
        else:
            return False
