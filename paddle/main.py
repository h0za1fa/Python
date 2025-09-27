import turtle as t
from paddle import Paddle 
from ball import Ball
from pongsetup import Setup
from scoreboard import ScoreBoard 
import time

def up_left():
    side.lefty.forward(10)

def down_left():
    side.lefty.backward(10)

screen = t.Screen()
screen.setup(600,400)
screen.listen()
screen.tracer(0)
screen.bgcolor('black')

side = Paddle ()
ball = Ball()
setgame = Setup()
scorebrd = ScoreBoard()


screen.onkeypress(lambda: side.lefty.forward(15) , "a")
screen.onkeypress(lambda: side.lefty.backward(15), 'd')
screen.onkeypress(lambda: side.righty.forward(15), 'j')
screen.onkeypress(lambda: side.righty.backward(15), 'l')


game_on = True
while game_on == True:
    scorebrd.update_score()
    
    screen.update()
    time.sleep(0.1)
    
    ball.forward(10)
    ball.physics(side.lefty,side.righty)
    
    if ball.xcor() > 295 :
        scorebrd.l_score_update()
        ball.ht()
        ball = Ball()
    if ball.xcor() < -295 :
        scorebrd.r_score_update()
        ball.ht()
        ball = Ball()

screen.exitonclick()