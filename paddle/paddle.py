from turtle import Turtle
class Paddle():
    def __init__(self):
        self.lefty = Turtle()
        self.righty = Turtle()
        self.left_side()
        self.right_side()
    
    def left_side(self):
        self.lefty.shape('square')
        self.lefty.color('white')
        self.lefty.shapesize(0.5,2)
        self.lefty.penup()
        self.lefty.goto(-275,0)
        self.lefty.setheading(90)
    
    def right_side(self):
        self.righty = Turtle()
        self.righty.shape('square')
        self.righty.color('white')
        self.righty.shapesize(0.5,2)
        self.righty.penup()
        self.righty.goto(275,0)
        self.righty.setheading(90)
