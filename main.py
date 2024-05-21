from turtle import Turtle, Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(),new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

screen = Screen()
screen.title("Pong Game!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

ball = Ball(0, 0)
scoreboard = Scoreboard()

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.listen()

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    ball.move()

    right_paddle.within_upper_bound()
    left_paddle.within_upper_bound()

    right_paddle.within_lower_bound()
    left_paddle.within_lower_bound()

    # Detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with r_paddle & l_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.distance(right_paddle) > 50 and ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss
    if ball.distance(left_paddle) > 50 and ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    screen.update()

screen.mainloop()