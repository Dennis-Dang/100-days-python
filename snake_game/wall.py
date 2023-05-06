from turtle import Turtle
from config import SCREEN_HEIGHT, SCREEN_WIDTH

PENSIZE = 20


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.hideturtle()
        self.pensize(PENSIZE)
        self.penup()
        self.wall_limit_x = SCREEN_WIDTH / 2
        self.wall_limit_y = SCREEN_HEIGHT / 2
        self.goto(self.wall_limit_x, self.wall_limit_y)
        self.pendown()
        for x in range(4):
            self.right(90)
            if x % 2 == 0:
                self.fd(SCREEN_HEIGHT)
            else:
                self.forward(SCREEN_WIDTH)
