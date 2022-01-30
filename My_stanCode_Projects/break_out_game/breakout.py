"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 60  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!
    lives = NUM_LIVES
    while lives > 0:
        # Pause
        pause(FRAME_RATE)
        # Update
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        # Check
        graphics.check_for_collisions()
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            graphics.bouncing_ball_x()
        if graphics.ball.y <= 0 or graphics.bricks_done():
            graphics.bouncing_ball_y()
        if graphics.ball_is_out():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()


if __name__ == '__main__':
    main()
