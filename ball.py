from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.penup()
        self.setheading(45)
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x=x, y=y)

    def bounce(self):
        self.ymove *= -1

    def paddle_bounce(self, x):
        if self.distance(x) < 60 and self.xcor() > 320 or self.distance(x) < 60 and self.xcor() > -320:
            self.xmove *= -1
            self.movespeed *= 0.9
