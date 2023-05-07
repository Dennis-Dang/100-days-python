from turtle import Screen
from paddle import Paddle

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Instantiate both paddles at their corresponding starting locations
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

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
    screen.update()

screen.exitonclick()
