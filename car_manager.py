from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square") 
        self.shapesize(stretch_len=5)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.randint(-200, 200))

    def move(self):
        self.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        speed = STARTING_MOVE_DISTANCE
        speed += MOVE_INCREMENT
        self.backward(speed)

