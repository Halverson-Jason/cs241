import arcade
import math
from flyingObject import FlyingObject
from point import Point
from velocity import Velocity

SPEED = 0.25
ROTATE_AMOUNT = 3

RADIUS = 45

class Ship(FlyingObject):
    def __init__(self,starting_point:Point):
        super().__init__(center=starting_point)
        self.angle = 0
        self.radius = RADIUS # I know this should be 30 but the size of the img is 99px wide so 45 is closer to radius
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
        # Enable for reverse thrusters
        # dx = math.cos(math.radians(self.angle + 90)) * SPEED
        # self.velocity.dx -= dx
        # dy = math.sin(math.radians(self.angle + 90)) * SPEED
        # self.velocity.dy -= dy
        self.velocity.dx = 0
        self.velocity.dy = 0
    def draw(self):
        img = "images/playerShip1_orange.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

