import turtle as t
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = t.Screen ()
screen . bgcolor('black')
screen . title ('Lets play pong!')
screen . setup (600,400)

# to setup the play are /// i tried to be cool so this is messed up..... im not cool :)
cen_line = t.Turtle ()
left_set = t.Turtle()
right_set = t.Turtle()
cen_line.ht()
cen_line.color('white')
cen_line.speed('slow')
left_set.ht()
left_set.color('white')
left_set.speed('slow')
right_set.ht()
right_set.color('white')
right_set.speed('slow')
left_set.penup()
right_set.penup()
left_set.goto(275,195)
right_set.goto(-275,-195)
left_set.pendown()
right_set.pendown()
left_set.goto(275,-195)
right_set.goto(-275,195)
left_set.goto(-275,-195)
right_set.goto(275,195)
cen_line.teleport(0,195)
cen_line.penup()
while cen_line.ycor() > -185 :
    cen_line.setheading(270)
    cen_line.forward(10)
    cen_line.pendown()
    cen_line.forward(10)
    cen_line.penup()

screen . tracer (0)
r_paddle = Paddle(275)
l_paddle = Paddle(-275)
ball = Ball()
score = ScoreBoard()

screen . listen()
screen . onkey( fun = l_paddle.move_up , key = 'w' )
screen . onkey( fun = l_paddle.move_down , key = 's' )
screen . onkey( fun = r_paddle.move_up , key = 'Up' )
screen . onkey( fun = r_paddle.move_down , key = 'Down' )

game_on = True
while game_on == True:
    time.sleep(ball.move_speed)
    ball.movement()
    score.update_score()
    
    # for bouncing off wall on y-axis
    if ball.ycor() > 195 or ball.ycor() < -195 :
        ball.y_bounce()
    
    # for bouncing off paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 255 or ball.distance(l_paddle) < 50 and ball.xcor() < -255 :
        ball.x_bounce()
    
    # for reseting after left paddle misses the ball
    if ball.xcor() < -275 :
        ball.reset_game()
        score.l_score_update()
    # for reseting after right paddle misses the ball
    if ball.xcor() > 275 :
        ball.reset_game()
        score.r_score_update()
    
    screen . update()   


screen . exitonclick()