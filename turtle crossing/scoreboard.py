from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-205, 250)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def add(self):
        self.level += 1
        self.update_score()
