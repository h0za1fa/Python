import turtle as tur
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r , g , b)
    return color

tur.colormode(255)

tim = tur.Turtle()
tim.speed(20)
tim.hideturtle()
tim.width(15)

headings = [0,90,270,180]

while True:
    tim.setheading(random.choice(headings))
    tim.forward(25)
    tim.color(random_color())

my_screen = Screen()
my_screen.exitonclick()