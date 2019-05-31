from point import Point
from velocity import Velocity
#TODO: add is_off_screen method
class FlyingObject:

    def __init__(self,starting_point,velocity):
        self.alive = True
        self.starting_point = starting_point
        self.velocity = velocity
        self.current_point = starting_point

    def isAlive(self):
        return self.alive

    def setPoint(self, point):
        self.current_point = point

    def getPoint(self):
        return self.current_point

    def setVelocity(self,velocity = None, dx = None, dy = None):
        if velocity != None:
            self.velocity = velocity
        elif dx != None and dy != None:
            self.velocity.set_dx(dx)
            self.velocity.set_dy(dy)

    def getVelocity(self):
        return self.velocity

    def advance(self):
        self.current_point.add_x(self.velocity.get_dx())
        self.current_point.add_y(self.velocity.get_dy())

    def kill(self):
        self.alive = False
