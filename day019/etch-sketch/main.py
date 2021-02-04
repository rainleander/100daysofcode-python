""""
Challenge:
Create a simple etch a sketch using turtle
Functionality:
W = Forwards
S = Backwards
A = Counter-Clockwise
D = Clockwise
C = Clear Drawing
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_screen():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()


screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
