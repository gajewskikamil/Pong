from turtle import Screen, Turtle
from paddle import SCREEN_WIDTH, SCREEN_HEIGHT

linecord_w = SCREEN_WIDTH - 10
linecord_h = SCREEN_HEIGHT - 2


class ScreenPong:
    def __init__(self):
        self.line = None
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.title("Pong")
        self.screen.tracer(0)
        self.screen.listen()
        self.frame()

    def listening(self, player_up, player_down, num_player):
        if num_player == 1:
            self.screen.onkeypress(player_up, "w")
            self.screen.onkeypress(player_down, "s")
        elif num_player == 2:
            self.screen.onkeypress(player_up, "Up")
            self.screen.onkeypress(player_down, "Down")

    def update(self):
        self.screen.update()

    def exitonclick(self):
        self.screen.exitonclick()

    def frame(self):
        self.line = Turtle()
        self.line.color('white')
        self.line.speed("fastest")
        self.line.hideturtle()
        self.line.penup()
        self.line.goto(linecord_w / 2, linecord_h / 2)
        self.line.pendown()
        self.line.setheading(270)
        self.line.forward(linecord_h)
        self.line.setheading(180)
        self.line.forward(linecord_w)
        self.line.setheading(90)
        self.line.forward(linecord_h)
        self.line.setheading(0)
        self.line.forward(linecord_w)
        self.line.backward(linecord_w / 2)
        self.line.setheading(270)
        for _ in range(int(linecord_h / 20)):
            self.line.pendown()
            self.line.forward(10.35)
            self.line.penup()
            self.line.forward(10.35)
