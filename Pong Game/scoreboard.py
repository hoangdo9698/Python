from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 320)
        self.write(self.left_score, align=ALIGN, font=FONT)
        self.goto(100, 320)
        self.write(self.right_score, align=ALIGN, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update()

    def right_point(self):
        self.right_score += 1
        self.update()
