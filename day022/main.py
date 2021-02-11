from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    elif ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    elif ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    elif ball.xcor() > 380:
        ball.goto(0, 0)
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.goto(0, 0)
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
