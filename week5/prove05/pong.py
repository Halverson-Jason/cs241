"""
File: pong.py
Original Author: Br. Burton
Designed to be completed by others
This program implements a simplistic version of the
classic Pong arcade game.
"""
import arcade
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get_center_x(self):
        return self.x
    def get_center_y(self):
        return self.y
    def set_y_center(self,y):
        self.y = y
    def set_x_center(self,x):
        self.x = x

class Velocity:
    def __init__(self,dx,dy):
        self.dx = dx
        self.dy = dx
    def set_dx(self,dx):
        self.dx = dx
    def set_dy(self,dy):
        self.dy = dy
    def get_dx(self):
        return self.dx
    def get_dy(self):
        return self.dy

class Ball:

    def __init__(self):
        self.restart()

    def draw(self):
        arcade.draw_circle_filled(self.center.get_center_x(),self.center.get_center_y(),BALL_RADIUS, arcade.color.GREEN)

    def advance(self):
        new_y_center = self.center.get_center_y() + self.velocity.get_dy()
        new_x_center = self.center.get_center_x() + self.velocity.get_dx()
        self.center.set_y_center(new_y_center)
        self.center.set_x_center(new_x_center)

    def bounce_horizontal(self):
        if self.velocity.get_dx() > 0:
            #TODO: Get rid of magic numbers
            new_dx = -(self.velocity.get_dx()+0.2)
        else:
            new_dx = -(self.velocity.get_dx()-0.2)

        self.velocity.set_dx(new_dx)

    def bounce_vertical(self):
        # This is to prevent too slow of a start
        if self.velocity.get_dy() > 0:
            new_dy = -(self.velocity.get_dy()+0.2)
        else:
            new_dy = -(self.velocity.get_dy()-0.2)

        self.velocity.set_dy(new_dy)

    def restart(self):
        x_center = 0 + BALL_RADIUS*2
        y_center = random.uniform(0,SCREEN_HEIGHT)
        x_velocity = random.uniform(-2,2)
        y_velocity = random.uniform(-2,2)

        # TODO: get rid of slow starts
        self.center = Point(x_center,y_center)
        self.velocity = Velocity(x_velocity,y_velocity)

class Paddle:

    def __init__(self):
        x_center = SCREEN_WIDTH - 20
        y_center = SCREEN_HEIGHT / 2
        self.center = Point(x_center,y_center)
    def draw(self):
        arcade.draw_rectangle_filled(self.center.get_center_x(),self.center.get_center_y(),PADDLE_WIDTH,PADDLE_HEIGHT, arcade.color.GREEN)
    def move_up(self):
        new_y_center = self.center.get_center_y() + MOVE_AMOUNT
        if (new_y_center + PADDLE_HEIGHT/2) < SCREEN_HEIGHT:
            self.center.set_y_center(new_y_center)

    def move_down(self):
        new_y_center = self.center.get_center_y() - MOVE_AMOUNT
        if (new_y_center - PADDLE_HEIGHT/2) > 0:
            self.center.set_y_center(new_y_center)

class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.ball.draw()
        self.paddle.draw()

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

        # Move the ball forward one element in time
        self.ball.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit()
        self.check_bounce()

    def check_hit(self):
        """
        Checks to see if the ball has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and
                    abs(self.ball.center.y - self.paddle.center.y) < too_close_y and
                    self.ball.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_horizontal()
            self.score += SCORE_HIT

    def check_miss(self):
        """
        Checks to see if the ball went past the paddle
        and if so, restarts it.
        """
        if self.ball.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.ball.restart()

    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        if self.ball.center.x < 0 and self.ball.velocity.dx < 0:
            self.ball.bounce_horizontal()

        if self.ball.center.y < 0 and self.ball.velocity.dy < 0:
            self.ball.bounce_vertical()

        if self.ball.center.y > SCREEN_HEIGHT and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_down()

        if self.holding_right:
            self.paddle.move_up()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False

# Creates the game and starts it going
window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()