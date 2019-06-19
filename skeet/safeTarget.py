from target import Target
import arcade
import random

class SafeTarget(Target):
    def __init__(self):
        super().__init__()
        self.radius = 40
        self.killPoints = -10
        self.lives = 1
        self.targetColor = arcade.color.RED
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y,self.radius,self.radius,self.targetColor)
