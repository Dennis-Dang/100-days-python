import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# By default, each block on the segment is size 20. Keep this in mind if you want to increase move distance.
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    # Create the snake with each segment at the defined coordinates defined in STARTING_POSITIONS
    # Segments should be square shaped and colored white.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = turtle.Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # Move the segments, except the head. Iterate in reverse order.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head
        self.segments[0].forward(MOVE_DISTANCE)
