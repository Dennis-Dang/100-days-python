from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.setheading(random.randrange(0, 360, 40))
        self.penup()

    def move(self):
        self.forward(10)

    def bounce_wall(self):
        self.setheading(-self.heading())

    def bounce_paddle(self):
        self.setheading(180 - self.heading())

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_paddle()
