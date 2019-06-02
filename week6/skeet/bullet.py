from flyingObject import FlyingObject
from point import Point
from velocity import Velocity
import arcade
import math

RADIUS = 3
BULLET_COLOR = arcade.color.BLUE
BULLET_SPEED = 10
#TODO: Refactor this
STARTING_X = 0
STARTING_Y = 0


class Bullet(FlyingObject):
    def __init__(self):
        self.current_point = Point(STARTING_X,STARTING_Y)
        super().__init__(self.current_point)
        self.radius = RADIUS
        self.isAlive = True

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)
    def fire(self, angle):
        self.velocity.set_dx(math.cos(math.radians(angle)) * BULLET_SPEED)
        self.velocity.set_dy(math.sin(math.radians(angle)) * BULLET_SPEED)
