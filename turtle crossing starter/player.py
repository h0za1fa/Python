from turtle import  Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.MOVE_DISTANCE = 10
        self.FINISH_LINE_Y = 280
        self.shape('turtle')
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
    
    def movement(self):
        new_y = self.ycor() + 10
        self.goto(0,new_y)
    