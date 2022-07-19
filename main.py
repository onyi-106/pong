from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Paddles
player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))

# Ball
ball = Ball()

# Scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")
screen.onkey(player_2.up, "Up")
screen.onkey(player_2.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    # print(ball.position())

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_shift *= -1

    # Detect collision with paddle
    if ball.distance(player_1) < 50 and ball.xcor() < -330:
        ball.x_shift *= -1
    if ball.distance(player_2) < 50 and ball.xcor() > 330:
        ball.x_shift *= -1

    # Detect out of bounds
    # Right side
    if ball.xcor() > 400:
        ball.home()
        ball.x_shift *= -1
        scoreboard.left_score += 1
        scoreboard.update_score()
    # Left side
    if ball.xcor() < -400:
        ball.home()
        ball.x_shift *= -1
        scoreboard.right_score += 1
        scoreboard.update_score()


screen.exitonclick()
