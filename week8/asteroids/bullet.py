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
    def __init__(self,starting_point):
        super().__init__(starting_point)
        self.radius = RADIUS
        self.isAlive = True
        self.angle = 0

    def draw(self):
        img = "images/laserBlue01.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency

        x = self.center.center_x
        y = self.center.center_y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
