import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. states naming game")
screen.register_shape("blank_states_img.gif")
image = "blank_states_img.gif"
screen.bgpic(image)

marker = turtle.Turtle()
marker.hideturtle()
marker.penup()
marker.color("black")


def mark_state(marker, answer):
    x_cord = int(data[data.state == answer].x.iloc[0])
    y_cord = int(data[data.state == answer].y.iloc[0])
    marker.goto(x_cord, y_cord)
    marker.write(answer)


score = 0
game_is_on = True
while game_is_on:
    guess = screen.textinput(title=f"Guess a state. {score}/50", prompt=f"Guess a state. {score}/50")
    guess = guess.title()
    if guess in states:
        score += 1
        mark_state(marker, guess)
        states.remove(guess)

    if score == 50:
        game_is_on = False
        print("Congrats! You named all 50 states! Here is a cookie: 🍪")

    if guess == "Exit":
        pandas.DataFrame(states).to_csv("states_to_study.csv")
        game_is_on = False
