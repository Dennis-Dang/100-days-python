from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        # Holds the score for the player on the left.
        self.l_score = 0
        # Holds the score for the player on the right.
        self.r_score = 0

        self.update_scoreboard()

    def left_scores(self, score):
        if score:
            self.l_score += 1
        else:
            self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 150)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))