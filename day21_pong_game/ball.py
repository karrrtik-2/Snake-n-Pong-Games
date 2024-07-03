from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.speed_move = 0.05
        
    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.penup()
        self.goto(new_xcor,new_ycor)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.speed_move *= 0.98
    
    def reset_position(self):
        self.goto(0,0)
        self.speed_move = 0.08
        self.bounce_x()