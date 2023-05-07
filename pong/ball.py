from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.setheading(random.randrange(0, 360, 40))
        self.penup()
        self.move_speed = 0.1

    def move(self):
        self.forward(10)

    def bounce_wall(self):
        self.setheading(180 - self.heading())

    def bounce_paddle(self):
        self.setheading(-self.heading())
        # Increases the difficulty by making animations faster every time the ball gets hit by a paddle.
        # 0.9 is a modifier multiplier that reduces the delay time (default at 0.1).
        self.move_speed *= 0.9
        print(f"Difficulty increased to: {self.move_speed}")

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle()
