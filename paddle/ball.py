from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pencolor('white')
        self.penup()
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.speed('fastest')
        self.play()
    
    
    def play(self):
        self.setheading(randint(0,360))
    
    def physics(self, left_paddle, right_paddle):
        if self.ycor() > 190 or self.ycor() < -190 :
            self.setheading(self.heading() * -1)
        
        if self.distance(left_paddle.xcor() - 30 , left_paddle.ycor()) < 40 or self.distance(right_paddle.xcor() + 30 , right_paddle.ycor()) < 40 :
            self.setheading(self.heading() + randint(140,220))