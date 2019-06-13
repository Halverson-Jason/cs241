import arcade
import math
from flyingObject import FlyingObject
from point import Point
from velocity import Velocity

SPEED = 0.25
ROTATE_AMOUNT = 3
class Ship(FlyingObject):
    def __init__(self):
        super().__init__()
        self.angle = 0
    def moveLeft(self):
        if self.angle < 0:
            self.angle = 359
        elif self.angle > 360:
            self.angle = 0
        else:
            self.angle += ROTATE_AMOUNT
    def moveRight(self):
        if self.angle < 0:
            self.angle = 359
        elif self.angle > 360:
            self.angle = 0
        else:
            self.angle -= ROTATE_AMOUNT
    def moveUp(self):

        dx = math.cos(math.radians(self.angle + 90)) * SPEED
        dy = math.sin(math.radians(self.angle + 90)) * SPEED
        self.velocity.dx += dx
        self.velocity.dy += dy
    def moveDown(self):
        dx = math.cos(math.radians(self.angle + 90)) * SPEED
        self.velocity.dx -= dx
        dy = math.sin(math.radians(self.angle + 90)) * SPEED
        self.velocity.dy -= dy
    def draw(self):
        img = "images/playerShip1_orange.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency

        x = self.center.center_x
        y = self.center.center_y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

