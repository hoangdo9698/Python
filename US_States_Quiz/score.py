from turtle import Turtle

ALIGN = "Center"
FONT = ("Courier", 18, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color("black")

    def update(self, score):
        self.goto(300, 300)
        self.clear()
        self.write(f"Score: {score}/50", align=ALIGN, font=FONT)

    def win(self):
        self.goto(0, 0)
        self.write("Well done! You have completed the challenge!", align=ALIGN, font=FONT)
