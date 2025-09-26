import turtle as t
import time
from snake import Snake

def left():
    snake.turn_left()

snake = Snake()
screen = t.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

for _ in range(10):
    snake.make_segments()

game_on = True
while game_on == True:
    screen.update()
    time.sleep(0.1)
    screen.onkeypress(snake.turn_left, "d")
    screen.onkeypress(snake.turn_right, "a")
    snake.movement()

screen.exitonclick()
