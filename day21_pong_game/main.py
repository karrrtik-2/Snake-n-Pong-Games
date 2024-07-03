import turtle as t
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PINGY PONGY GAME")
screen.tracer(0)

r_paddle = Paddle(360,0)
l_paddle = Paddle(-360,0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down,'s')

game_is_on = True
while game_is_on: 
    time.sleep(ball.speed_move)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collision with r_paddle or l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r paddle misses ball
    if ball.xcor() > 380:
        score.update_l()
        ball.reset_position()

    # detect l paddle misses ball
    if ball.xcor() < -380:
        score.update_r()
        ball.reset_position()
    
screen.exitonclick()