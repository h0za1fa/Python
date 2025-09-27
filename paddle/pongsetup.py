from turtle import Turtle

class Setup(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.ht()
        self.setup()
        self.boundry()
    
    def setup(self):
        self.teleport(0,190)
        self.setheading(270)
        while self.ycor() != -190 :
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
    
    def boundry(self):
        self.goto(300,200)
        self.pendown()
        self.goto(300,-200)
        self.goto(-300,-200)
        self.goto(-300,200)
        self.goto(300,200)