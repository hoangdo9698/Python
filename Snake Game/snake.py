from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake = []
        self.snake_form()
        self.head = self.snake[0]

    def snake_form(self):
        for pos in POSITION:
            self.add_body(pos)

    def snake_reset(self):
        for each_snake in self.snake:
            each_snake.goto(2000,2000)
        self.snake.clear()
        self.snake_form()
        self.head = self.snake[0]

    def add_body(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake.append(new_snake)

    def extend(self):
        self.add_body(self.snake[-1].position())

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for num in range(len(self.snake) - 1, 0, -1):
            x = self.snake[num - 1].xcor()
            y = self.snake[num - 1].ycor()
            self.snake[num].goto(x, y)
        self.head.forward(DISTANCE)
