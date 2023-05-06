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


class Game:
    def __init__(self):
        self.pause = True


game = Game()


def pause_game(the_game):
    the_game.pause ^= the_game.pause
    if the_game.pause:
        food.hideturtle()
        snake.hide(the_game.pause)
    else:
        food.showturtle()
        snake.hide(the_game.pause)


# Add listener
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=lambda: pause_game(game), key="Return")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    print(game.pause)
    if not game.pause:
        snake.move()

        # Detect food collision
        if snake.head.distance(food) < 15.0:
            food.refresh()
            # Increment 1 to score.
            scoreboard.increase_score()
            snake.extend()

        # Detect wall collision
        if snake.head.xcor() > wall.wall_limit_x \
                or snake.head.ycor() > wall.wall_limit_y \
                or snake.head.xcor() < -wall.wall_limit_x \
                or snake.head.ycor() < -wall.wall_limit_y:
            game_is_on = False
            scoreboard.game_over()

        # Detect Tail collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
