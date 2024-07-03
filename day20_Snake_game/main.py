import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = t.Screen()
screen.title("SAANP KA KHEL")
screen.setup(width=600,height=600)
screen.bgcolor("black")

screen.tracer(0)
saanp = Snake()
khana = Food()
score = ScoreBoard()
# key presses
screen.listen()
screen.onkey(saanp.up,'Up')
screen.onkey(saanp.down,'Down')
screen.onkey(saanp.right,'Right')
screen.onkey(saanp.left,'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)

    saanp.move()

    # saanp eats khana
    if saanp.head.distance(khana) < 15:
        khana.refresh()
        saanp.extend()
        score.increase_score()
        score.update()
    
    # detects wall collision
    if saanp.head.xcor() > 290 or saanp.head.xcor() < -290 or saanp.head.ycor() > 290 or saanp.head.ycor() < -290:
        score.reset()
        saanp.reset()  
    
    # detects tail collision
    for segment in saanp.three_chintus[1:]:
        if saanp.head.distance(segment) < 10:
            score.reset()
   
screen.exitonclick()