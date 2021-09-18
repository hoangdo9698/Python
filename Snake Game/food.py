from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0) #fastest
        self.penup()
        self.color("green")
        self.new_position()

    def new_position(self):
        x = random.randint(-14, 14)*20
        y = random.randint(-14, 14)*20
        self.goto(x, y)


