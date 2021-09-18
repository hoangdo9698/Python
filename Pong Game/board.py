from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.shape("square")
        self.speed(0)
        self.penup()
        self.goto(0, 290)
        self.right(90)
        self.pensize(5)
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.goto(-450, -300)
        self.left(90)
        self.pendown()
        for i in range(2):
            self.forward(900)
            self.left(90)
            self.forward(600)
            self.left(90)
