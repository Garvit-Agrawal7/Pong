from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
t1 = Turtle()
t2 = Turtle()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

l_score = 0
r_score = 0
while True:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    ball.paddle_bounce(r_paddle)
    ball.paddle_bounce(l_paddle)

    if ball.xcor() > 365:
        ball.goto(0, 0)
        ball.setheading(135)
        l_score += 1
        t1.clear()
        ball.movespeed = 0.1
    elif ball.xcor() < -365:
        ball.goto(0, 0)
        ball.setheading(45)
        r_score += 1
        t2.clear()
        ball.movespeed = 0.1
    t1.goto(x=-100, y=250)
    t1.color("white")
    t1.hideturtle()
    t1.write(l_score, move=False, align='center', font=('arial', 30, 'normal'))

    t2.goto(x=100, y=250)
    t2.color("white")
    t2.hideturtle()
    t2.write(r_score, move=False, align='center', font=('arial', 30, 'normal'))
