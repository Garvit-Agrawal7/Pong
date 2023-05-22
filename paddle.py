from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x[0], y=0)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
