import turtle as t

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake():
    #constructor
    def __init__(self):
        self.x=0
        self.three_chintus = []
        self.snake_body()
        self.head = self.three_chintus[0]

    # creating snake body
    def snake_body(self):
        self.x = 0
        for length in range(3):
            self.add_segment(length)
    
    def add_segment(self,position):
        chintu = t.Turtle('square')
        chintu.speed('fastest')
        chintu.color('white')
        chintu.penup()
        chintu.goto(self.x,0)
        self.three_chintus.append(chintu)
        self.x-=20

    def reset(self):
        for seg in self.three_chintus:
            seg.goto(1000,1000)
        self.three_chintus.clear()
        self.snake_body()
        self.head = self.three_chintus[0]

    def extend(self):
        self.add_segment(self.three_chintus[-1].position())

    # SNAKE MOVEMENT(-moving lower body along with head simultaneously)
    def move(self):
        for segment in range(len(self.three_chintus)-1,0,-1):
            new_x = self.three_chintus[segment-1].xcor()
            new_y = self.three_chintus[segment-1].ycor()
            self.three_chintus[segment].penup()
            self.three_chintus[segment].goto(new_x,new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        