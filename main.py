import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

screen.listen()

player = Player()
scoreboard = Scoreboard()

ls_cars = []
for i in range(0, 30):
    new_car = CarManager()
    ls_cars.append(new_car)


screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    for car in ls_cars:
        car.move()
        if car.offscreen():
            car.place()

        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False

        if player.distance(car) < 25 and abs(player.ycor() - car.ycor()) < 4:
            scoreboard.game_over()
            game_is_on = False


    if player.at_finish_line():
        player.reset()
        scoreboard.increase()
        for car in ls_cars:
            car.next_level()

    if scoreboard.last_level():
        scoreboard.end()
        game_is_on = False

    time.sleep(0.1)
    screen.update()

screen.exitonclick()