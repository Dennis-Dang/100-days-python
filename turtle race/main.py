from typing import Final
import turtle as t
import random

# Canvas size
WINDOW_HEIGHT: Final = 700
WINDOW_WIDTH: Final = 600

# Padding to prevent spawning turtles right next to each other (shoulder to shoulder)
# see function go_to_start()
PADDING: Final = 10

screen = t.Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
num_pos_turtles = WINDOW_HEIGHT/19

colors = ["red", "orange", "yellow", "green", "blue", "purple", "tan", "aquamarine"]


def create_colored_turtles():
    turtle_list = []
    for i in range(len(colors)):
        racer = t.Turtle(shape='turtle')
        racer.penup()
        randomColor = random.choice(colors)
        racer.color(randomColor)
        colors.remove(randomColor)
        turtle_list.append(racer)
    return turtle_list


def draw_finishline():
    finishline = t.Turtle()
    finishline.color("red")
    finishline.hideturtle()
    finishline.penup()
    finishline.goto(int(t.window_width() / 2), int(-t.window_height() / 2))
    finishline.pendown()
    finishline.goto(int(t.window_width() / 2), int(t.window_height() / 2))


def go_to_start(turtle_list):
    num_turtles = len(turtle_list)

    # Padding to prevent spawning turtles right next to each other (shoulder to shoulder)
    # Each turtle is 40 height. Plus one to draw them next to each other without overlapping.
    # In this case, padding is accounted in turtle border.
    turtle_size = 20 + 1 + PADDING

    # Initialization of the turtle's position is at the world origin (0,0).
    # Distance from the origin to the world's left (or right) border is WINDOW_WIDTH / 2.
    # the -0.90 is just a percentage of how much of that distance to the left should the turtle be positioned.
    starting_pos_x = t.window_width() / 2 * -0.90

    # Calculates the starting y coordinate of the first turtle.
    # I wanted the turtles to be lined up symmetrically against the x-axis.
    # The sum of all the turtle's height together will be the total distance.
    # total_height = turtle_size * num_turtles
    # But because the origin is the midpoint of symmetry, we divide this distance by 2.
    # Hence, we are left with the offsets from 0.
    # offset = total_height / 2
    starting_y = -turtle_size*num_turtles/2
    for i in range(num_turtles):
        # turtle_size*i accounts for how much to add up from the starting y position of the loop, depending on how many
        # turtles there are
        turtle_list[i].goto(x=starting_pos_x, y=starting_y+turtle_size*i)


race_is_on = False

racers = create_colored_turtles()
draw_finishline()
go_to_start(racers)

user_bet = t.textinput("Who's going to win?", "Who's going to win?\n Type a color: ")
if user_bet:
    race_is_on = True
else:
    exit()

# max_x = -sys.maxsize
# min_x = sys.maxsize
#
# for (x,y) in vector:
#     if x > max_x:
#         max_x = x
#
#     if x < min_x:
#         min_x = x
#
# print(f"min x: {min_x}, max x: {max_x})")
while race_is_on:
    for turtle in racers:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        # Check if the turtle has gone past the finish line.
        # turtle.xcor() returns the center turtle object. Add 20 to offset to the turtle's head facing east.
        if turtle.xcor()+20 > int((t.window_width()/2)):
            race_is_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The winning turtle was {turtle.pencolor()}.")

            else:
                print(f"Sorry, you didn't guess right. The winning turtle was {turtle.pencolor()}.")
            print(f"Turtle's absolute location is: {turtle.xcor()} turtle's head is at: {turtle.xcor()+9}")
            break

screen.exitonclick()
