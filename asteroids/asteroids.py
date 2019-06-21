#!/usr/bin/env python3
"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
from ship import Ship
from bullet import Bullet
from point import Point
from meteor import Meteor
from largeMeteor import LargeMeteor

#TODO: http://arcade.academy/examples/instruction_and_game_over_screens.html
#TODO: Add class method to flyingobject to set game state like screen width

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GAME_TEXT_COORD_X = 150

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

MACHINE_GUN_WAIT = 5

NUMBER_OF_STARTING_METEORS = 5

SHIP_START_X = 250
SHIP_START_Y = 250

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.machineGunWait = MACHINE_GUN_WAIT

        self.setup()

    def setup(self):
        self.held_keys = set()
        ship_starting_point = Point(SHIP_START_X,SHIP_START_Y)

        self.ship = Ship(ship_starting_point)
        self.bullets = []
        self.meteors = []
        for new_meteor in range(NUMBER_OF_STARTING_METEORS):
            #TODO: pass a new meteor that creates large meteor
            new_meteor = LargeMeteor()
            self.meteors.append(new_meteor)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        #evaluate if game over/won
        if not self.ship.alive:
            self.game_over()
        elif not self.meteors:
            self.game_won()

        # draw each object
        self.ship.draw()
        for bullet in self.bullets:
            bullet.draw()
        for meteor in self.meteors:
            meteor.draw()
        self.ship.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # Check for collisions
        self.check_collisions()

        self.check_keys()

        # Tell everything to advance or move forward one step in time
        self.ship.advance()
        for bullet in self.bullets:
            bullet.advance()
        for meteor in self.meteors:
            meteor.advance()

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        for bullet in self.bullets:
            for meteor in self.meteors:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and meteor.alive:
                    bullet_too_close = bullet.radius + meteor.radius

                    if (abs(bullet.center.x - meteor.center.x) < bullet_too_close and
                                abs(bullet.center.y - meteor.center.y) < bullet_too_close):
                        # its a hit!
                        bullet.kill()
                        meteor.split(self.meteors)

        for meteor in self.meteors:
            if self.ship.alive and meteor.alive:
                too_close = self.ship.radius + meteor.radius
                if (abs(self.ship.center.x - meteor.center.x) < too_close and abs(self.ship.center.y - meteor.center.y) < too_close):
                    # its a hit!
                    self.ship.kill()

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

        for meteor in self.meteors:
            if not meteor.alive:
                self.meteors.remove(meteor)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.moveLeft()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.moveRight()

        if arcade.key.UP in self.held_keys:
            self.ship.moveUp()

        if arcade.key.DOWN in self.held_keys:
            self.ship.moveDown()

        # Machine gun mode...
        if arcade.key.SPACE in self.held_keys:
            # Wait for machine gun so it's not a stream
            if self.machineGunWait == 0:
                starting_point = self.ship.center.copy()
                newbullet = Bullet(starting_point, self.ship.angle)
                self.bullets.append(newbullet)
                self.machineGunWait = MACHINE_GUN_WAIT
            else:
                self.machineGunWait -= 1


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                starting_point = self.ship.center.copy()
                newbullet = Bullet(starting_point, self.ship.angle)
                self.bullets.append(newbullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
    def game_over(self):
        """
        Puts Game Over on the screen
        """
        text = "Game Over"
        start_x = GAME_TEXT_COORD_X
        start_y = SCREEN_HEIGHT / 2
        arcade.draw_text(text, start_x=start_x, start_y=start_y, font_size=72, color=arcade.color.RED)
    def game_won(self):
        """
        Puts Game Over on the screen
        """
        text = "You Won!!!"
        start_x = GAME_TEXT_COORD_X
        start_y = SCREEN_HEIGHT / 2
        arcade.draw_text(text, start_x=start_x, start_y=start_y, font_size=72, color=arcade.color.GREEN)
# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()