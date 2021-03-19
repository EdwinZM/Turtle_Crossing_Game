import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
score = Scoreboard()

screen.onkey(key="Up", fun= player.up)
screen.onkey(key="Down", fun= player.down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    
    cars.move()

    if player.ycor() > 280:
            player.finish_line()
            score.victory()
            cars.increase_speed()
    
    for car in cars.all_cars:
        if player.distance(car) <= 20:
            game_is_on = False
            score.defeat()

screen.exitonclick()