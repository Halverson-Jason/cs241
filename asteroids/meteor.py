import arcade
from abc import ABC
from abc import abstractmethod
from flyingObject import FlyingObject
from point import Point
import random

class Meteor(FlyingObject,ABC):
    def __init__(self,starting_point = None):
        super().__init__()
        if starting_point == None:
            random.seed()
            STARTING_X = random.randint(150,300)
            STARTING_Y = 0

            self.center.x = STARTING_X
            self.center.y = STARTING_Y

        else:
            self.center.x = starting_point.center.x
            self.center.y = starting_point.center.y

        self.rotation = 0
        self.rotation_direction = random.uniform(-1,1)
        self.angle = 0
        self.hit = False
        self.img = ""
        self.radius = 1

    def draw(self):

        texture = arcade.load_texture(self.img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency

        x = self.center.x
        y = self.center.y
        self.rotation += self.rotation_direction
        angle = self.rotation

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
    @abstractmethod
    def split(self,meteorList: list):
        pass
