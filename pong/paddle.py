from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1.0, stretch_len=5.0)
        self.setheading(90)
        self.goto(x, y)

    def up(self):
        if -240 <= self.ycor()+20 <= 240:
            self.forward(20)

    def down(self):
        if -240 <= self.ycor()-20 <= 240:
            self.backward(20)
