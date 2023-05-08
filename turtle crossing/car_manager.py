from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_len=2)
        self.starting_y_pos = random.randint(-250, 250)
        self.goto(300, self.starting_y_pos)

    def move(self):
        self.forward(MOVE_INCREMENT)

    def reset_pos(self):
        self.goto(300, self.starting_y_pos)


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(1, 10) == 1:
            self.all_cars.append(Car())
        print(len(self.all_cars))

    def move_cars(self):
        for car in self.all_cars:
            if car.xcor() < -300:
                car.hideturtle()
                self.all_cars.remove(car)
                print(len(self.all_cars))
            car.move()
