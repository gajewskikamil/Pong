from turtle import Turtle

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

LEFT_PADDLE = (-SCREEN_WIDTH / 2 + 20, 0)
RIGHT_PADDLE = (SCREEN_WIDTH / 2 - 20, 0)

UP = 90.0
DOWN = 270.0

#
# class Paddle:
#     def __init__(self, player):
#         self.paddle = Turtle("square")
#         self.paddle.color("white")
#         self.paddle.pensize(20)
#         self.paddle.shapesize(0.5, 5, 1)
#         self.paddle.penup()
#         self.paddle.setheading(UP)
#         if player == 1:
#             self.paddle.goto(LEFT_PADDLE)
#         elif player == 2:
#             self.paddle.goto(RIGHT_PADDLE)
#
#     def up(self):
#         if self.paddle.ycor() < SCREEN_HEIGHT/2 - 50:
#             self.paddle.forward(30)
#             return True
#         else:
#             return False
#     def down(self):
#         if self.paddle.ycor() > SCREEN_HEIGHT/-2 + 50:
#             self.paddle.forward(-30)
#             return True
#         else:
#             return False
#
#     def opponent_move(self, who):
#         if who == "computer":
#             if self.paddle.heading() == UP:
#                 if self.paddle.ycor() < SCREEN_HEIGHT/2 - 50:
#                     self.paddle.forward(30)
#                 else:
#                      self.paddle.setheading(DOWN)
#             elif self.paddle.heading() == DOWN:
#                 if self.paddle.ycor() > SCREEN_HEIGHT/-2 + 50:
#                     self.paddle.forward(30)
#                 else:
#                     self.paddle.setheading(UP)
#         if who == "player":
#             return False


SEGMENTS = 5


class Paddle:
    def __init__(self, player):
        self.paddlelist = []
        for _ in range(SEGMENTS):
            segment = Turtle("square")
            segment.color("white")
            segment.pensize(20)
            segment.shapesize(0.1, 1, 1)
            segment.penup()
            self.paddlelist.append(segment)
        if player == 1:
            for i in range(SEGMENTS):
                self.paddlelist[i].goto(LEFT_PADDLE)
                self.paddlelist[i].setheading(UP)
            self.paddlelist[0].sety(30)
            self.paddlelist[1].sety(15)
            self.paddlelist[3].sety(-15)
            self.paddlelist[4].sety(-30)
        elif player == 2:
            for i in range(SEGMENTS):
                self.paddlelist[i].goto(RIGHT_PADDLE)
                self.paddlelist[i].color("Blue")
                self.paddlelist[i].setheading(UP)
            self.paddlelist[0].sety(30)
            self.paddlelist[1].sety(15)
            self.paddlelist[3].sety(-15)
            self.paddlelist[4].sety(-30)

    def up(self):
        if self.paddlelist[0].ycor() < SCREEN_HEIGHT / 2 - 10:
            for i in range(SEGMENTS):
                self.paddlelist[i].forward(30)
            return True
        else:
            return False

    def down(self):
        if self.paddlelist[2].ycor() > SCREEN_HEIGHT / -2 + 50:
            for i in range(SEGMENTS):
                self.paddlelist[i].forward(-30)
            return True
        else:
            return False

    def opponent_move(self, who):
        if who == "computer":
            if self.paddlelist[0].heading() == UP:
                if self.paddlelist[0].ycor() < SCREEN_HEIGHT / 2 - 10:
                    for i in range(SEGMENTS):
                        self.paddlelist[i].forward(30)
                else:
                    for i in range(SEGMENTS):
                        self.paddlelist[i].setheading(DOWN)
            elif self.paddlelist[2].heading() == DOWN:
                if self.paddlelist[2].ycor() > SCREEN_HEIGHT / -2 + 50:
                    for i in range(SEGMENTS):
                        self.paddlelist[i].forward(30)
                else:
                    for i in range(SEGMENTS):
                        self.paddlelist[i].setheading(UP)
        if who == "player":
            return False
