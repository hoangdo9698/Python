from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_control = 0.05
        self.x_moving = 10
        self.y_moving = 10

    def move(self):
        x = self.xcor() + self.x_moving
        y = self.ycor() + self.y_moving
        self.goto(x, y)

    def bounce_y(self):
        self.y_moving *= -1

    def bounce_x(self):
        self.x_moving *= -1
        self.speed_control *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.speed_control = 0.05
        self.bounce_x()
