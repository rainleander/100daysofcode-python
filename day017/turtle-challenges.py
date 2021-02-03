#####Turtle Intro######
from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")

# tim.right(90)
# tim.backward(200)
# tim.left(180)
# tim.setheading(0)

######## Challenge 1 - Draw a Square ############

# for x in range(4):
#     tim.forward(100)
#     tim.right(90)

# import villains
#
# print(villains.gen())

########### Challenge 2 - Draw a Dashed Line ########

# for x in range(15):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

########### Challenge 3 - Draw Shapes ########

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# With random colors for each shape

t.colormode(255)


def random_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    tim.color(R, G, B)


# sides = 3
#
# for x in range(7):
#     random_color()
#     angle = 360 / sides
#     for y in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1

########### Challenge 4 - Draw a Random Walk ########

# tim.pensize(10)
# tim.speed("fastest")
# directions = [0, 90, 180, 270]
#
# for x in range(200):
#     random_color()
#     tim.forward(50)
#     tim.setheading(random.choice(directions))
#

########### Challenge 5 - Spirograph ########

# draw a circle with a diameter of 100, random colors, that repeats per two degrees to create a spirograph

tim.speed("fastest")
tim.hideturtle()

for x in range(73):
    y = 5
    random_color()
    tim.circle(100)
    tim.left(y)
    y += 5

screen = Screen()
screen.exitonclick()
