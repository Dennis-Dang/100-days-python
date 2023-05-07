from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.setheading(random.randrange(0, 360, 40))
        self.penup()

    def move(self):
        if self.ycor() <= -280 or self.ycor() >= 280:
            self.setheading(-self.heading())
        self.forward(10)
