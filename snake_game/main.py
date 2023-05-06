from turtle import Screen, Turtle
import time
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from wall import Wall

# Setup Screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake game")
# Turn off animations, allows manual control over graphical updates
screen.tracer(0)

# Create wall
wall = Wall()


# Create snake
snake = Snake()

# Create Food
food = Food()

# Create ScoreBoard
scoreboard = ScoreBoard()

# Add listener
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15.0:
        food.refresh()
        # Increment 1 to score.
        scoreboard.increase_score()

    # Detect wall collision
    if snake.head.xcor() > wall.wall_limit_x \
            or snake.head.ycor() > wall.wall_limit_y \
            or snake.head.xcor() < -wall.wall_limit_x \
            or snake.head.xcor() < -wall.wall_limit_y:
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()

