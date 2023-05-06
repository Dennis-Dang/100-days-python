import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# By default, each block on the segment is size 20. Keep this in mind if you want to increase move distance.
MOVE_DISTANCE = 20

# turtle.Turtle Heading constants for directions.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Create the snake with each segment at the defined coordinates defined in STARTING_POSITIONS
    # Segments should be square shaped and colored white.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # requires a 'position' to add a segment to
    def add_segment(self, position):
        new_segment = turtle.Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Uses the Turtle position() method to return the absolute (x, y) coordinates
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the segments, except the head. Iterate in reverse order.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def hide(self, hide):
        if hide:
            for segment in self.segments:
                segment.hideturtle()
        else:
            for segment in self.segments:
                segment.showturtle()
