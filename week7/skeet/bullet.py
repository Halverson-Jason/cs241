flyingObject.py                                                                                     0000664 0001750 0001750 00000001734 13476356106 013077  0                                                                                                    ustar   jason                           jason                                                                                                                                                                                                                  from point import Point
from velocity import Velocity

class FlyingObject:
    """The FlyingObject has all the"""
    def __init__(self,starting_point):
        self.alive = True
        self.velocity = Velocity(0,0)
        self.center = starting_point

    def isAlive(self):
        return self.alive

    def setPoint(self, point):
        self.center = point

    def setVelocity(self,velocity = None, dx = None, dy = None):
        if velocity != None:
            self.velocity = velocity
        elif dx != None and dy != None:
            self.velocity.set_dx(dx)
            self.velocity.set_dy(dy)

    def advance(self):
        self.center.add_x(self.velocity.dx)
        self.center.add_y(self.velocity.dy)

    def kill(self):
        self.alive = False

    def is_off_screen(self,screen_width,screen_height):
        if self.center.x < 0 or self.center.x > 600 or self.center.y < 0 or self.center.y > 500 :
            return True
        else:
            return False
                                    point.py                                                                                            0000664 0001750 0001750 00000000620 13476354522 011602  0                                                                                                    ustar   jason                           jason                                                                                                                                                                                                                  class Point:
    def __init__(self,x=None,y=None):
        if x == None and y == None:
            self.x = 0
            self.y = 0
        else:
            self.x = x
            self.y = y
    def get_center_x(self):
        return self.x
    def get_center_y(self):
        return self.y
    def add_x(self, dx):
        self.x = self.x + dx
    def add_y(self, dy):
        self.y = self.y + dy                                                                                                                safeTarget.py                                                                                       0000664 0001750 0001750 00000000576 13475645025 012550  0                                                                                                    ustar   jason                           jason                                                                                                                                                                                                                  from target import Target
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
                                                                                                                                  skeet.py                                                                                            0000664 0001750 0001750 00000015217 13475643107 011573  0                                                                                                    ustar   jason                           jason                                                                                                                                                                                                                  """
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
import arcade
import math
import random

from bullet import Bullet
from point import Point
from target import Target
from standardTarget import StandardTarget
from strongTarget import StrongTarget
from safeTarget import SafeTarget

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15




class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # TODO: iterate through your targets and draw them...
        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()
        #Re-seed random
        random.seed()
        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        #Decide what type of target to create and append it to the list
        targetNumber = random.randint(1, 3)
        if targetNumber == 1:
            target = StandardTarget()
        elif targetNumber == 2:
            target = StrongTarget()
        elif targetNumber == 3:
            target = SafeTarget()

        self.targets.append(target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()                                                                                                                                                                                                                                                                                                                                                                                 standardTarget.py                                                                                   0000664 0001750 0001750 00000000506 13476355002 013415  0                                                                                                    ustar   jason                           jason                                                                                                                                                                                                                  from target import Target
import arcade
import random

class StandardTarget(Target):
    def __init__(self):
        super().__init__()
        self.radius = 20
        self.killPoints = 1
        self.lives = 1
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.targetColor)                                                                                                                                                                                          strongTarget.py                                                                                     0000664 0001750 0001750 00000001344 13475645142 013140  0                                                                                                    ustar   jason                           jason                                                                                                                                                                                                                  from target import Target
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
                                                                                                                                                                                                                                                                                            target.py                                                                                           0000664 0001750 0001750 00000001574 13476355302 011745  0                                                                                                    ustar   jason                           jason                                                                                                                                                                                                                  from flyingObject import FlyingObject
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
        pass                                                                                                                                    velocity.py                                                                                         0000664 0001750 0001750 00000000263 13476355265 012317  0                                                                                                    ustar   jason                           jason                                                                                                                                                                                                                  class Velocity:
    def __init__(self,dx,dy):
        self.dx = dx
        self.dy = dx
    def set_dx(self,dx):
        self.dx = dx
    def set_dy(self,dy):
        self.dy = dy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             