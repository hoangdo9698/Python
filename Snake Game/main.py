from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision
    if snake.head.distance(food) < 15:
        food.new_position()
        scoreboard.update()
        snake.extend()

    # wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        # game_on = False
        # scoreboard.game_over()
        scoreboard.game_reset()
        snake.snake_reset()

    # body collision
    for body_part in snake.snake[1:]:
        if snake.head.distance(body_part) < 10:
            # game_on = False
            # scoreboard.game_over()
            scoreboard.game_reset()
            snake.snake_reset()

screen.exitonclick()
