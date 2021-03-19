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
car = CarManager()
score = Scoreboard()

screen.onkey(key="Up", fun= player.up)
screen.onkey(key="Down", fun= player.down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.move()
 
    if player.ycor() > 280:
        player.finish_line()
        score.victory()
        car.increase_speed()
    
    if player.distance(car) < 50 and player.xcor == car.xcor():
        game_is_on = False
        score.defeat()

