from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.left_score = 0
        self.right_score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-50,-30)
        self.write(self.right_score, False , 'center' , ('ariel',40,'normal'))
        self.goto(50,-30)
        self.write(self.left_score, False , 'center' , ('ariel',40,'normal'))
    
    def l_score_update(self):
        self.left_score += 1
    
    def r_score_update(self):
        self.right_score += 1