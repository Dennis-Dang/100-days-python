from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    """The `Car` object that moves horizontally from the right to left edges of the screen."""
    def __init__(self):
        """Creates a `Turtle` object with the following characteristics: \n
            Random `color` (from COLORS list), \n
            `Size` of 40x20 pixels, \n
            Spawns at x-coordinate `300`, which is at the right edge of the screen, at a `random` y-coordinate

        """
        super().__init__(shape="square")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_len=2)
        # 250 is chosen as a boundary so that the obstacles do not spawn too close to the top or bottom of the screen.
        # Ample space is allowed for the turtle to move in the obstacle zone, and to move out of it to advance levels.
        self.starting_y_pos = random.randint(-250, 250)
        self.goto(300, self.starting_y_pos)

    def move(self, amount):
        """Moves the turtle towards the left edge of the screen. The constant defined MOVE_INCREMENT determines the
        distance all car objects will advance forward eat time."""
        self.forward(amount)


class CarManager:
    """Manages a collection of Car objects."""
    def __init__(self):
        """The constructor initializes an empty list called all_cars to later manage the collection of cars."""
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Constructs, and then adds a `Car` object to the car collection list. This process has a 1 in 10 chance of
        executing in order to prevent accumulating a large collection list."""
        if random.randint(1, 10) == 1:
            self.all_cars.append(Car())

    def move_cars(self):
        """Moves all cars contained in the collection list. If the car goes past the left-edge of the screen, remove it
        from the collection. Removing the car from the collection reduces accumulating a large collection list."""
        for car in self.all_cars:
            if car.xcor() < -300:
                car.hideturtle()
                self.all_cars.remove(car)
            car.move(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

