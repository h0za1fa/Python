COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(1,2)
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.color_select()
        self.starting_pos()
        self.MOVE_INCREMENT = 10
    
    def movement(self):
        new_x = self.xcor() - self.MOVE_INCREMENT
        self.goto(new_x,self.ycor())
    
    def color_select(self):
        self.color(random.choice(self.colors))
    
    def starting_pos(self):
        new_y = random.randint(-250 , 250)
        self.goto(300,new_y)
    
    def level_up(self):
        self.MOVE_INCREMENT += 2