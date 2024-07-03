from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()
        self.goto(xcor,ycor)

    def up(self):
        new_ycor = self.ycor() + 25
        self.goto(self.xcor(),new_ycor)

    def down(self):
        new_ycor = self.ycor() - 25
        self.goto(self.xcor(),new_ycor)