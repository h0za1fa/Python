import turtle as t

class Snake:
    def __init__(self):
        self.segments = []
        self.n_x = 0

    def make_segments(self):
        tim = t.Turtle()
        tim.penup()
        tim.color('white')
        tim.shape('square')
        tim.width(20)
        tim.goto(self.n_x,0)
        self.n_x -= 20
        self.segments.append(tim)
    
    def turn_left(self):
        tuleft = self.segments[0].heading() - 90
        self.segments[0].setheading(tuleft)
    
    def turn_right(self):
        turight = self.segments[0].heading() + 90
        self.segments[0].setheading(turight)
    
    def movement(self):
        for var in range (len(self.segments) - 1 , 0 , -1):
            new_x = self.segments[var-1].xcor()
            new_y = self.segments[var-1].ycor()
            self.segments[var].goto( new_x , new_y )
        self.segments[0].forward(20)
    
    def self_collision(self):
        if len(self.segments) > 5:
            for n in range (5 , len(self.segments) - 1):
                if self.segments[0].distance(self.segments[n]) < 1 :
                    return True
            return False