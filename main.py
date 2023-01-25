import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.title('Turtle-crossing')
screen.bgpic('ezgif.com-gif-maker (1).gif')
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
time_delay = 0.1
car_manager = CarManager()
car_manager.create_cars()
screen.listen()
screen.onkey(player.move,'Up')
game_is_on = True
while game_is_on:
    time.sleep(player.time_delay)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()

    for cars in car_manager.all_turtles:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

    if player.finish_line():
        player.go_to_start()
        scoreboard.increase_level()

screen.exitonclick()