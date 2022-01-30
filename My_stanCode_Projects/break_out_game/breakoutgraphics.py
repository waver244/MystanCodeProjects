"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    # Constructor
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-paddle_width)/2, y=self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.open1 = False
        onmouseclicked(self.start_game)
        onmousemoved(self.change_position)

        # Draw bricks
        self.brick_num = brick_rows*brick_cols
        self.count_bricks = 0
        for j in range(brick_rows):
            for i in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=i*brick_width+i*brick_spacing, y=j*brick_height+j*brick_spacing)
                brick.filled = True
                c = random.randint(1, 6)
                if c == 1:
                    brick.fill_color = 'gray'
                elif c == 2:
                    brick.fill_color = 'darkgreen'
                elif c == 3:
                    brick.fill_color = 'lightgreen'
                elif c == 4:
                    brick.fill_color = 'green'
                elif c == 5 or c == 6:
                    brick.fill_color = 'white'
                self.window.add(brick)

    # Detect mouse position
    def change_position(self, event):
        if event.x-(self.paddle.width/2) <= 0:
            self.window.add(self.paddle, x=0, y=self.paddle.y)
        elif event.x+(self.paddle.width/2) > self.window.width:
            self.window.add(self.paddle, x=self.window.width-self.paddle.width, y=self.paddle.y)
        else:
            self.window.add(self.paddle, x=event.x - self.paddle.width / 2, y=self.paddle.y)

    # Return dx
    def get_dx(self):
        return self.__dx

    # Return dy
    def get_dy(self):
        return self.__dy

    # Reset ball to the middle of window and reset dx and dy to zero
    def reset_ball(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2, y=(self.window.height - self.ball.height) / 2)
        self.open1 = False
        self.__dx = 0
        self.__dy = 0

    # Check if ball is out of window
    def ball_is_out(self):
        ball_is_out = self.ball.y > self.window.height
        return ball_is_out

    # Set ball velocity randomly
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # When mouse click, start the game
    def start_game(self, event):
        if not self.open1:
            self.set_ball_velocity()
            self.open1 = True

    # Bouncing ball (dx)
    def bouncing_ball_x(self):
        self.__dx = -self.__dx

    # Bouncing ball (dy)
    def bouncing_ball_y(self):
        self.__dy = -self.__dy

    # Check if all bricks are removed
    def bricks_done(self):
        bricks_done = False
        if self.count_bricks == self.brick_num:
            bricks_done = True
        return bricks_done

    # Check for collisions (maybe brick or paddle)
    def check_for_collisions(self):
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at((self.ball.x + self.ball_radius * 2), self.ball.y)
        obj3 = self.window.get_object_at(self.ball.x, (self.ball.y + self.ball_radius * 2))
        obj4 = self.window.get_object_at((self.ball.x + self.ball_radius * 2), (self.ball.y + self.ball_radius * 2))
        if obj1 is not None:
            if obj1 is not self.paddle:
                if self.__dy < 0:
                    the_brick = self.window.get_object_at(obj1.x, obj1.y)
                    self.bouncing_ball_y()
                    self.window.remove(the_brick)
                    self.__dx = random.randint(1, MAX_X_SPEED)
                    self.count_bricks += 1
            elif obj1 is self.paddle:
                if self.__dy > 0:
                    self.bouncing_ball_y()
                    self.__dx = random.randint(1, MAX_X_SPEED)
        if obj2 is not None:
            if obj2 is not self.paddle:
                if self.__dy < 0:
                    the_brick = self.window.get_object_at(obj2.x, obj2.y)
                    self.bouncing_ball_y()
                    self.window.remove(the_brick)
                    self.__dx = random.randint(1, MAX_X_SPEED)
                    self.count_bricks += 1
            elif obj2 is self.paddle:
                if self.__dy > 0:
                    self.bouncing_ball_y()
                    self.__dx = random.randint(1, MAX_X_SPEED)
        if obj3 is not None:
            if obj3 is not self.paddle:
                if self.__dy < 0:
                    the_brick = self.window.get_object_at(obj3.x, obj3.y)
                    self.bouncing_ball_y()
                    self.window.remove(the_brick)
                    self.__dx = random.randint(1, MAX_X_SPEED)
                    self.count_bricks += 1
            elif obj3 is self.paddle:
                if self.__dy > 0:
                    self.bouncing_ball_y()
                    self.__dx = random.randint(1, MAX_X_SPEED)
        if obj4 is not None:
            if obj4 is not self.paddle:
                if self.__dy < 0:
                    the_brick = self.window.get_object_at(obj4.x, obj4.y)
                    self.bouncing_ball_y()
                    self.window.remove(the_brick)
                    self.__dx = random.randint(1, MAX_X_SPEED)
                    self.count_bricks += 1
            elif obj4 is self.paddle:
                if self.__dy > 0:
                    self.bouncing_ball_y()
                    self.__dx = random.randint(1, MAX_X_SPEED)











