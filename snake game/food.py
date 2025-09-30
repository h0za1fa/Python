from turtle import Turtle 
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.shapesize(0.5 , 0.5)
        self.penup()
        x_axis = random.randint(-27,27) * 10
        y_axis = random.randint(-27,27) * 10
        self.goto(x_axis,y_axis)
        self.refresh()
    
    def refresh(self):
        x_axis = random.randint(-28,28) * 10
        y_axis = random.randint(-28,28) * 10
        self.goto(x_axis,y_axis)