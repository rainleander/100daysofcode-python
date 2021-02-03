from turtle import Screen
import turtle
import random

# import colorgram
# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
#
# iteration = 0
#
# for x in colors:
#     print(colors[iteration].rgb)
#     iteration += 1
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(182, 163, 132), (144, 162, 183), (125, 98, 68), (179, 151, 164), (82, 99, 127), (123, 82, 97),
              (164, 151, 54), (213, 203, 140), (147, 171, 157), (63, 37, 25), (68, 24, 34), (86, 111, 92),
              (160, 106, 125), (32, 42, 63), (101, 122, 167), (108, 39, 57), (210, 180, 192), (177, 189, 212),
              (167, 111, 97), (82, 87, 20), (211, 183, 177), (105, 44, 36), (169, 204, 189), (104, 144, 118),
              (41, 59, 100), (38, 53, 45)]

tim = turtle.Turtle()
turtle.colormode(255)
tim.up()
tim.speed("fastest")


def dot_row():
    for _ in range(10):
        dot_color = random.choice(color_list)
        tim.dot(20, dot_color)
        tim.up()
        tim.fd(50)


y_coordinate = -250.00

for x in range(10):
    tim.goto(-250.00, y_coordinate)
    dot_row()
    y_coordinate += 50.00

screen = Screen()
screen.exitonclick()
