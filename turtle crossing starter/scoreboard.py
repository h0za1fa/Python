FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-220,250)
        self.level = 1
        self.write(f'level {self.level}', move=False, align='center', font=("Courier", 24, "normal"))
    
    def levelup(self):
        self.clear()
        self.level += 1
        self.write(f'level {self.level}', move=False, align='center', font=("Courier", 24, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write('Game over!', move=False, align='center', font=("Courier", 50, "normal"))