from target import Target
import arcade
import random

class StrongTarget(Target):
    def __init__(self):
        super().__init__()
        self.radius = 20
        self.killPoints = 5
        self.lives = 3
        self.targetColor = arcade.color.BLACK

        x_velocity = random.uniform(1.0,3.0)
        y_velocity = random.uniform(-2.0,3.0)
        self.velocity.set_dx(x_velocity)
        self.velocity.set_dy(y_velocity)

    def draw(self):
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, self.targetColor)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, self.targetColor, font_size=20)
