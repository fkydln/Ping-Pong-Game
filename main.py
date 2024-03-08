from turtle import Turtle, Screen

faz = Turtle()
screen = Screen()
# screen.screensize(canvwidth=800, canvheight=600)
screen.setup(width=800, height=600)
screen.bgcolor('gray')
screen.title('Pong')


screen.exitonclick()