from paddle import Paddle, SCREEN_HEIGHT, SCREEN_WIDTH
from ball import Ball
from screen_pong import ScreenPong, linecord_h
from scoreboard import Scoreboard
import time

screen = ScreenPong()
opponent = "player"

player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball()
player1_scoreboard = Scoreboard(-SCREEN_HEIGHT / 3, SCREEN_WIDTH / 3.3)
player2_scoreboard = Scoreboard(SCREEN_HEIGHT / 3, SCREEN_WIDTH / 3.3)
gameover = Scoreboard(0, 0)

player1_scoreboard.update_score()
player2_scoreboard.update_score()

screen.listening(player1.up, player1.down, 1)
times = 0.031
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(times)
    if player2_scoreboard.score == 10:
        gameover.game_over("player2")
        game_is_on = False
    if player1_scoreboard.score == 10:
        gameover.game_over("player1")
        game_is_on = False
    if not player2.opponent_move(opponent):
        screen.listening(player2.up, player2.down, 2)
    ball.move()

    if ball.xcor() >= SCREEN_WIDTH / 2:
        player1_scoreboard.increase_score()
        ball.start_pos()
    if ball.xcor() <= -SCREEN_WIDTH / 2:
        player2_scoreboard.increase_score()
        ball.start_pos()
    if ball.ycor() >= linecord_h / 2:
        ball.setheading(-ball.heading())
    if ball.ycor() <= -linecord_h / 2:
        ball.setheading(-ball.heading())

    if ball.distance(player1.paddlelist[0]) <= 20:
        if 90 < ball.heading() < 270:
            ball.setheading(180 - ball.heading() + 10)
        print(f"player1 turn to {ball.heading()}")
    if ball.distance(player1.paddlelist[1]) <= 20:
        if 90 < ball.heading() < 270:
            ball.setheading(180 - ball.heading())
        print(f"player1 turn to {ball.heading()}")
    if ball.distance(player1.paddlelist[2]) <= 20:
        if 90 < ball.heading() < 270:
            ball.setheading(180 - ball.heading())
        print(f"player1 turn to {ball.heading()}")
    if ball.distance(player1.paddlelist[3]) <= 20:
        if 90 < ball.heading() < 270:
            ball.setheading(180 - ball.heading())
        print(f"player1 turn to {ball.heading()}")
    if ball.distance(player1.paddlelist[4]) <= 20:
        if 90 < ball.heading() < 270:
            ball.setheading(180 - ball.heading() - 10)
        print(f"player1 turn to {ball.heading()}")

    if ball.distance(player2.paddlelist[0]) <= 20:
        if ball.heading() in range(0, 90):
            ball.setheading(180 - ball.heading() - 10)
        if ball.heading() in range(270, 360):
            ball.setheading(180 - ball.heading() - 10)
        print(f"player2 turn to {ball.heading()}")
    if ball.distance(player2.paddlelist[1]) <= 20:
        if ball.heading() in range(0, 90):
            ball.setheading(180 - ball.heading())
        if ball.heading() in range(270, 360):
            ball.setheading(180 - ball.heading())
        print(f"player2 turn to {ball.heading()}")
    if ball.distance(player2.paddlelist[2]) <= 20:
        if ball.heading() in range(0, 90):
            ball.setheading(180 - ball.heading())
        if ball.heading() in range(270, 360):
            ball.setheading(180 - ball.heading())
        print(f"player2 turn to {ball.heading()}")
    if ball.distance(player2.paddlelist[3]) <= 20:
        if ball.heading() in range(0, 90):
            ball.setheading(180 - ball.heading())
        if ball.heading() in range(270, 360):
            ball.setheading(180 - ball.heading())
        print(f"player2 turn to {ball.heading()}")
    if ball.distance(player2.paddlelist[4]) <= 20:
        if ball.heading() in range(0, 90):
            ball.setheading(180 - ball.heading() + 10)
        if ball.heading() in range(270, 360):
            ball.setheading(180 - ball.heading() + 10)
        print(f"player2 turn to {ball.heading()}")

screen.update()
screen.exitonclick()
