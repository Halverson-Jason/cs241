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
            
            self.center.center_x = STARTING_X
            self.center.center_y = STARTING_Y
            
        else:
            self.center.center_x = starting_point.center.center_x
            self.center.center_y = starting_point.center.center_y

        x_velocity = 0
        y_velocity = 0
        self.velocity.dx = x_velocity
        self.velocity.dy = y_velocity
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

        x = self.center.center_x
        y = self.center.center_y
        self.rotation += self.rotation_direction
        angle = self.rotation

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
    @abstractmethod
    def split(self,meteorList: list):
        pass
