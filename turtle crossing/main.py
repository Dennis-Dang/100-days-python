import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkeypress(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        # Cars are 20 pixels in height, 40 pixels in width
        if car.distance(player) < 20:
            game_is_on = False
            car_manager.hide_all_cars()
            player.hideturtle()
            scoreboard.game_over()
            screen.update()

    if player.ycor() >= FINISH_LINE_Y:
        player.reset_pos()
        scoreboard.add()
        car_manager.level_up()

screen.exitonclick()