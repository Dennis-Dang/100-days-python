from turtle import Screen
import time
from snake import Snake
from food import Food
from config import SCREEN_WIDTH, SCREEN_HEIGHT


# Setup Screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake game")
# Turn off animations, allows manual control over graphical updates
screen.tracer(0)

# Create snake
snake = Snake()

# Create Food
food = Food()

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
screen.exitonclick()

