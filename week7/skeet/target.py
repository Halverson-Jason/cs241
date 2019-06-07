from flyingObject import FlyingObject
from point import Point
from abc import ABC
from abc import abstractclassmethod

import arcade
import random

class Target(FlyingObject,ABC):
    def __init__(self):
        self.killPoints = 1
        self.lives = 1
        self.targetColor = arcade.color.BLUE
        random.seed()
        STARTING_X = 0
        STARTING_Y = random.uniform(150,300)
        current_point = Point(STARTING_X,STARTING_Y)
        super().__init__(current_point)

        x_velocity = random.uniform(1.0,5.0)
        y_velocity = random.uniform(-2.0,5.0)
        self.velocity.set_dx(x_velocity)
        self.velocity.set_dy(y_velocity)

    def hit(self):
        if self.lives <= 1:
            self.alive = False
            return self.killPoints
        else:
            self.lives -= 1
            return 0

    @abstractclassmethod
    def draw(self):
        pass