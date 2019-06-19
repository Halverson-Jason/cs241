from flyingObject import FlyingObject
from point import Point
from velocity import Velocity
import arcade
import math

RADIUS = 5
BULLET_COLOR = arcade.color.BLUE
BULLET_SPEED = 10
#TODO: Refactor this
STARTING_X = 0
STARTING_Y = 0
INITIAL_HEALTH = 60
ANGLE_ADJUSTMENT = 90



class Bullet(FlyingObject):
    def __init__(self,starting_point, angle):
        super().__init__()
        self.center = starting_point
        self.health = INITIAL_HEALTH
        self.radius = RADIUS
        self.angle = angle + ANGLE_ADJUSTMENT
        self.fire(self.angle)

    def draw(self):
        img = "images/laserBlue01.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
    def advance(self):
        super().advance()
        self.health -= 1
        if self.health < 0:
            self.alive = False
