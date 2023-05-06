from turtle import Turtle
from config import SCREEN_HEIGHT

title_y_pos = SCREEN_HEIGHT/2 * 0.85

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.setposition(0, title_y_pos)
        self.score = -1
        self.increase_score()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

