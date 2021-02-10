from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.bgcolor("black")
screen.title("PONG!")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

ball = Ball()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 400 or ball.ycor() < -400:
        game_is_on = False



screen.exitonclick()
