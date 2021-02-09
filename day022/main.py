from turtle import Screen, Turtle

screen = Screen()
paddle_right = Turtle()

screen.bgcolor("black")
screen.title("PONG!")
screen.setup(width=800, height=600)

paddle_right.penup()
paddle_right.color("white")
paddle_right.shape("square")
paddle_right.shapesize(stretch_wid=1, stretch_len=5)
paddle_right.setheading(90)
paddle_right.setposition(350, 0)


def paddle_right_up():
    paddle_right.forward(20)


def paddle_right_down():
    paddle_right.backward(20)


screen.listen()
screen.onkey(paddle_right_up, "Up")
screen.onkey(paddle_right_down, "Down")

screen.exitonclick()
