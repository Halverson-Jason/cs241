from target import Target
import arcade
import random

class StandardTarget(Target):
    def __init__(self):
        super().__init__()
        self.radius = 20
        self.killPoints = 1
        self.lives = 1
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.targetColor)