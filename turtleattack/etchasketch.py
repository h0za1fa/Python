import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forw():
    tim.forward(10)
def move_back():
    tim.backward(10)
def move_left():
    tim.forward(1)
    tim.left(5)
def move_right():
    tim.forward(1)
    tim.right(5)
def clear_screen():
    tim.clear()

screen.listen()

screen.onkeypress(key='w' , fun = move_forw)
screen.onkeypress(key='s' , fun = move_back)
screen.onkeypress(key='d' , fun = move_right)
screen.onkeypress(key='a' , fun = move_left)
screen.onkeypress(key='c' , fun = clear_screen)


screen.exitonclick()