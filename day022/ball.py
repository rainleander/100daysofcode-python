from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)


    def move_right(self):
        random_y = random.randint(-300, 300)
        self.speed("slow")
        self.goto(400, random_y)


    def move_left(self):
        random_y = random.randint(-300, 300)
        self.speed("slow")
        self.goto(-400, random_y)
