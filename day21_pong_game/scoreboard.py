from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()
    
    def update(self):
        self.clear()
        self.goto(-100,190)
        self.write(self.l_score, align= 'center' , font=('Courier',80,'normal'))
        self.goto(100,190)
        self.write(self.r_score, align= 'center' , font=('Courier',80,'normal'))

    def update_r(self):
        self.r_score += 1
        self.update()

    def update_l(self):
        self.l_score += 1
        self.update()