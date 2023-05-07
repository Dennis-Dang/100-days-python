from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.setheading(random.randint(91, 269))
        self.penup()

    def move(self):
        self.forward(10)
