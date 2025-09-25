import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('normal')

def random_color():
    r = random.randint (0 , 255)
    g = random.randint (0 , 255)
    b = random.randint (0 , 255)
    return ( r , g , b )

for ang in range (72):
    tim.color(random_color())
    tim.setheading(ang*5)
    tim.circle(100)

my_screen = t.Screen()
my_screen.exitonclick()