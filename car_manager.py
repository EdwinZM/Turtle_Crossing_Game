from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        self.random_chance = random.randint(1, 6)
        if self.random_chance == 1:
            self.car = Turtle()
            self.car.shape("square") 
            self.car.shapesize(stretch_len=2)
            self.car.color(random.choice(COLORS))
            self.car.penup()
            self.car.goto(300, random.randint(-250, 250))
            self.all_cars.append(self.car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        speed = STARTING_MOVE_DISTANCE
        speed += MOVE_INCREMENT
        for car in self.all_cars:
            car.backward(speed)

