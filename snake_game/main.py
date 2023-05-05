from turtle import Screen, Turtle
import time


# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
# Turn off animations, allows manual control over graphical updates
screen.tracer(0)

# Create snake body
# Three turtle objects, each squared shape, colored white
starting_positions = [(0,0), (-20,0), (-40, 0)]
segments = []
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Move the segments, except the head. Iterate in reverse order.
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    # Now move the head.
    segments[0].forward(20)

screen.exitonclick()

















screen.exitonclick()