from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            lane = random.randint(-225, 225)
            new_car.goto(300, lane)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
