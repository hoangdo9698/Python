from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() <= 230:
            y = self.ycor() + 20
            x = self.xcor()
            self.goto(x, y)

    def down(self):
        if self.ycor() >= -230:
            y = self.ycor() - 20
            x = self.xcor()
            self.goto(x, y)


