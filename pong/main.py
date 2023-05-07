from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Instantiate both paddles at their corresponding starting locations
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# Instantiate the ball
ball = Ball()

scoreboard = Scoreboard()

# Event listener setup
# Even though I have an n-key rollover keyboard, I cannot move both paddles simultaneously.
# I believe this is a limitation of the turtle module itself. May consider the pygame module if simultaneous keypress
# is a necessary feature.
screen.listen()
screen.onkeypress(fun=l_paddle.up, key="Up")
screen.onkeypress(fun=l_paddle.down, key="Down")
screen.onkeypress(fun=r_paddle.up, key="w")
screen.onkeypress(fun=r_paddle.down, key="s")

# Main game loop
game_is_on = True
while game_is_on:
    # time.sleep controls how fast the animations go. The lower the number, the faster the animation speed is.
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Ball to wall collision detection
    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.bounce_wall()

    # Ball to paddle collision detection
    # If the ball is close to the x-coordinate bounding lines nearest to the center, and if the ball is less than 50
    # distance away, then it has collided with the paddle.
    # Additional notes:
    # The (+/-) 30 value is the offset of the ball size.
    # The (+-) 350 should be the x coordinates of the left and right paddles.
    if (ball.xcor() <= -350+30 and ball.distance(l_paddle) < 50) \
            or (ball.xcor() >= 350-30 and ball.distance(r_paddle) < 50):
        ball.bounce_paddle()

    # Detect Left Paddle misses
    if ball.xcor() < -380:
        scoreboard.left_scores(False)
        ball.reset_position()

    # Detect Right Paddle misses
    if ball.xcor() > 380:
        scoreboard.left_scores(True)
        ball.reset_position()
screen.exitonclick()
