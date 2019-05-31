from flyingObject import FlyingObject
from point import Point
from velocity import Velocity
import arcade

RADIUS = 3
BULLET_COLOR = "blue"
#TODO: Refactor this
STARTING_X = 0
STARTING_Y = 0
STARTING_VELOCITY = Velocity(3,3)

class Bullet(FlyingObject):
    def __init__(self):
        self.starting_point = Point(STARTING_X,STARTING_Y)
        super().__init__(self.starting_point,STARTING_VELOCITY)
        self.radius = RADIUS

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)

    def fire(self,angle):
        self.isAlive = True


# +is_off_screen(screen_width, screen_height) : Boolean
# +fire(angle:float) : None