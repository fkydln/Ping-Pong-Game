from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.change_x = 10
        self.change_y = 10

    def move(self):
        new_x = self.xcor() + self.change_x
        new_y = self.ycor() + self.change_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        if self.ycor() > 290:
            self.change_y *= -1
        elif self.ycor() < -280:
            self.change_y *= -1
    def bounce_x(self):
        self.change_x *= -1

