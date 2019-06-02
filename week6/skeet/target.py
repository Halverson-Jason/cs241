from flyingObject import FlyingObject
from point import Point
import arcade
import random

TARGET_COLOR = arcade.color.BLACK
#TODO: Refactor this
STARTING_X = 0
STARTING_Y = random.uniform(200,400)


class Target(FlyingObject):
    def __init__(self):
        self.current_point = Point(STARTING_X,STARTING_Y)
        super().__init__(self.current_point)
        #TODO: fix magic numbers
        self.radius = 20
        #TODO: Set velocity / fix magic numbers to random
        x_velocity = random.uniform(-2,5)
        y_velocity = random.uniform(1,5)
        self.velocity.set_dx(x_velocity)
        self.velocity.set_dy(y_velocity)
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, TARGET_COLOR)
    def hit(self):
        #TODO: fix magic numbers
        self.alive = False
        return 1
