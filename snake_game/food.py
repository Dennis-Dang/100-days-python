from turtle import Turtle
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT

max_x_distance = int(SCREEN_WIDTH/2 * 0.90)
max_y_distance = int(SCREEN_HEIGHT/2 * 0.90)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-max_x_distance, max_x_distance)
        random_y = random.randint(-max_y_distance, max_y_distance)
        self.goto(random_x, random_y)