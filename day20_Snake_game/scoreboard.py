from turtle import Turtle  
ALIGNMENT = 'center'
FONT = ("Courier",22,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        with open("day20_Snake_game/data.txt",mode='r') as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color('white')
        self.write(f"Score:{self.score} High Score: {self.highscore}",align=ALIGNMENT,font=FONT)

    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.write("GAME OVER.",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("day20_Snake_game/data.txt",mode='w') as data:
                data.write(f"{self.highscore}")
        self.score = 0 
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.highscore}",align=ALIGNMENT,font=FONT)
        
    def increase_score(self):
        self.score+=1
        self.update()