from turtle import Turtle, Screen

paddle = Turtle()
# left_paddle = Turtle()
screen = Screen()
# screen.screensize(canvwidth=800, canvheight=600)
screen.setup(width=800, height=600)
screen.bgcolor('gray')
screen.title('Pong')
screen.tracer(0)

paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1, outline=None)
paddle.penup()

paddle.setpos(x=350, y=0)

# left_paddle.shape('square')
# left_paddle.color('white')
# left_paddle.shapesize(stretch_wid=5, stretch_len=1, outline=None)
# left_paddle.penup()
# left_paddle.goto(x=-350, y=0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)



screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()