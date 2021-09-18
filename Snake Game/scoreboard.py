from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data_file.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGN, font=FONT)

    def update(self):
        self.score += 1
        self.write_score()

    def game_reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data_file.txt", mode ="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
