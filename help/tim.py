import arcade
import math
import random
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
SCORE = 0
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
        self.targets = []
        '''
        For Rifle movement functionality
        '''
        self.holding_left = False
        self.holding_right = False
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
        
        '''
        For Rifle movement functionality
        '''
        self.check_keys()
        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()
        for bullet in self.bullets:
            bullet.advance()
        for target in self.targets:
            target.advance()
    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """
        
        rand = random.randint(1,3)
        
        if rand == 1:
            target = StandardTarget()
        elif rand == 2:
            target = StrongTarget()
        elif rand == 3:
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
                    too_close = BULLET_RADIUS + TARGET_RADIUS
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
    
    '''
    For Rifle movement functionality
    '''
    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT:
            self.holding_left = True
        if key == arcade.key.RIGHT:
            self.holding_right = True
    
    '''
    For Rifle movement functionality
    '''
    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT:
            self.holding_left = False
        if key == arcade.key.RIGHT:
            self.holding_right = False
    
    '''
    For Rifle movement functionality
    '''
    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.rifle.move_left()
        if self.holding_right:
            self.rifle.move_right()
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        if x < self.rifle.center.x:
            self.rifle.angle = self._get_angle_degrees(x, y) - x
        else:
            self.rifle.angle = self._get_angle_degrees(x, y)
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)
        bullet = Bullet()
        bullet.fire(angle, self.rifle)
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
class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.center.x = RIFLE_HEIGHT
        self.center.y = 0
        self.angle = 45
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)
    '''
    For Rifle movement functionality
    '''
    def move_left(self):
        if self.center.x > RIFLE_HEIGHT / 2:
            self.center.x -= 5
                
    def move_right(self):
        if self.center.x < SCREEN_WIDTH - RIFLE_HEIGHT / 2:
            self.center.x += 5
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
class Velocity:
    def __init__(self):
        self.dx = 1
        self.dy = 1
        
class FlyingObjects:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
    
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, 75, 50, arcade.color.BLACK)
    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.center.x < 0 or self.center.x >= SCREEN_WIDTH:
            self.alive = False
            return True
        else:
            return False
class Bullet(FlyingObjects):
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        
    def fire(self, angle, rifle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
        self.center.x = rifle.center.x
        self.center.y = rifle.center.y
        
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BULLET_RADIUS, BULLET_COLOR)
class Target(FlyingObjects):
    def __init__(self):
        super().__init__()
        self.hits = 1
        self.typeOfTarget = 0
        self.center = Point()
        self.radius = TARGET_RADIUS        
        self.velocity = Velocity()
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-2, 5)
        self.center.x = random.uniform(1, SCREEN_WIDTH / 2)
        self.center.y = random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT - 1)
    
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, arcade.color.GREEN)
    
    def hit(self):
        self.alive = False
        return 1
        
    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.center.x < 0 or self.center.x >= SCREEN_WIDTH:
            self.alive = False
            return True
        else:
            return False
class StandardTarget(Target):
    def __init__(self):
        super().__init__()
        self.typeOfTarget = 1
    
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, arcade.color.GREEN)    
        
class StrongTarget(Target):
    def __init__(self):
        super().__init__()
        self.hits = 3
        self.typeOfTarget = 2
        self.velocity.dx = random.uniform(1, 3)
        self.velocity.dy = random.uniform(-2, 3)
    
    def draw(self):
        arcade.draw_circle_outline(self.center.x, self.center.y, TARGET_RADIUS, arcade.color.GREEN)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.hits), text_x, text_y, TARGET_COLOR, font_size=20)
        
    def hit(self):
        while self.hits >= 2:
            self.alive = True
            self.hits -= 1
            return 1
        else:
            self.alive = False
            self.hits -= 1
            return 5
        
class SafeTarget(Target):
    def __init__(self):
        super().__init__()
        self.typeOfTarget = 3
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, 40, 40, arcade.color.BLUE)
    
    def hit(self):
        self.alive = False
        return -10
def main():
    # Creates the game and starts it going
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
    
if __name__ == "__main__":
    main()