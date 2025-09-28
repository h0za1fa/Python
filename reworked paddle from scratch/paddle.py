import turtle as t

class Paddle(t.Turtle):
    def __init__(self, x_var):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5,1)
        self.penup()
        self.x_init = x_var
        self.goto(self.x_init,0)
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_init,new_y)
    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.x_init,new_y)