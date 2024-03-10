from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
# screen.screensize(canvwidth=800, canvheight=600)
screen.setup(width=800, height=600)
screen.bgcolor('gray')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
game_speed = 0.1


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    ball.bounce_y()
    time.sleep(game_speed)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        game_speed = game_speed - 0.01
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        game_speed = game_speed - 0.01

    if ball.xcor() > 380:
        print("Score goes to Left Paddle")
        scoreboard.l_point()
        ball.goto(0,0)
        ball.bounce_x()
    elif ball.xcor() < -380:
        print("Score goes to Right Paddle")
        scoreboard.r_point()
        ball.goto(0, 0)
        ball.bounce_x()

screen.exitonclick()