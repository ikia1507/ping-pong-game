import turtle as t
import time as tm
from PADDLE import Paddle
from BALL import Ball
from SCOREBOARD import Scoreboard

is_game_on=True
screen=t.Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=700, canvheight=700)
screen.tracer(0)
screen.listen()

position1=(345,25)
position2=(-345,25)
paddle_l=Paddle(position1)
paddle_r=Paddle(position2)
ball=Ball()
screen.onkey(paddle_r.move_up,"w")
screen.onkey(paddle_r.move_down,"s")
screen.onkey(paddle_l.move_up,"Up")
screen.onkey(paddle_l.move_down,"Down")
"""
paddle=t.Turtle(shape="square")
paddle.shapesize(5,1)
paddle.color("white")
paddle.penup()
paddle.setposition(345,25)
"""
scoreA=-175
scoreboard_a=Scoreboard(scoreA,player="A")
scoreA=175
scoreboard_b=Scoreboard(scoreA,player="B")

while is_game_on:
    screen.update()
    tm.sleep(ball.speed_parameter)
    if ball.ycor() >347 or ball.ycor()<-347:
        ball.bounce_boundary()
    # detection of collision with the paddle
    if (ball.distance(paddle_l)<50 and ball.xcor()>330) or (ball.distance(paddle_r)<50 and ball.xcor()<-330):
        ball.bounce_paddle()
    # detection of collision with the side walls
    if ball.xcor()>360 :
        ball.restart()
        scoreboard_a.scores()
    if ball.xcor()<-360 :
        ball.restart()
        scoreboard_b.scores()
    ball.move_ball()


screen.exitonclick()