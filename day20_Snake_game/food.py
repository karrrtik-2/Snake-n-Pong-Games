from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_cor = random.randint(-280,280)
        random_cor = random.randint(-280,280)
        self.goto(random_cor,random_cor)



        