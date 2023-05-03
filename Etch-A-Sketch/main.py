import turtle as t

tom = t.Turtle()
screen = t.Screen()


def move_forward():
    tom.fd(20)


def move_backward():
    tom.bk(20)


def turn_counterclockwise():
    tom.left(10)


def turn_clockwise():
    tom.right(10)


def reset():
    t.resetscreen()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='b', fun=move_backward)
screen.onkey(key='a', fun=turn_counterclockwise)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='c', fun=reset)

screen.exitonclick()