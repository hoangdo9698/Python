from turtle import Screen
from paddle import Paddle
from board import Board
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
board = Board()
scoreboard = Scoreboard()
ball = Ball()

paddle = Paddle((-430, 0))
pc_paddle = Paddle((430, 0))

screen.bgcolor("black")
screen.setup(1000, 800)
screen.title("Pong Game")
screen.listen()

screen.onkey(key="w", fun=paddle.up)
screen.onkey(key="s", fun=paddle.down)
screen.onkey(key="Up", fun=pc_paddle.up)
screen.onkey(key="Down", fun=pc_paddle.down)

game = True
while game:
    time.sleep(ball.speed_control)
    screen.update()
    ball.move()

    # wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # paddle bounce
    if ball.distance(paddle) < 50 and ball.xcor() < -400 or ball.distance(pc_paddle) < 50 and ball.xcor() > 400:
        ball.bounce_x()

    # score ball
    if ball.xcor() > 500:
        ball.ball_reset()
        scoreboard.left_point()

    if ball.xcor() < -500:
        ball.ball_reset()
        scoreboard.right_point()


screen.exitonclick()
