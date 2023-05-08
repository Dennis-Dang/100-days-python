from turtle import Turtle
from config import SCREEN_HEIGHT

title_y_pos = SCREEN_HEIGHT/2 * 0.85

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
positions = {
    "score": (0, title_y_pos),
    "game_over": (0, 0),
    "intro": (0, 30)
}

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(positions["score"])
        self.score = -1
        self.increase_score()
        self.paused = True
        self.intro()

    def update_scoreboard(self):
        self.clear()
        self.goto(positions["score"])
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def pause(self):
        self.paused ^= self.paused

    def game_over(self):
        self.goto(positions["game_over"])
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def intro(self):
        self.goto(positions["intro"])
        self.write("Press Enter to Start", align=ALIGNMENT, font=FONT)
