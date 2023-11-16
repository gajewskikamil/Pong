from random import choice
from turtle import Turtle

list_of_heading = [360, 45, 30, 180, 135, 120, 255, 230, 315, 330]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.pensize(20)

    def move(self):
        self.forward(10)

    def start_pos(self):
        rand = choice(list_of_heading)
        self.setheading(rand)
        self.setposition(0, 0)
