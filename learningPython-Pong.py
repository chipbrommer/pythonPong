# Learning Python
# Programmer: Chip Brommer
# Contact: Fredrick.Brommer@usm.edu
# Purpose: This is a simple python project to create the game 'Pong' using Python programming language.

import turtle   # turtle module for basic graphics
import os
import sys


# Creating game window,
    # Setting the windows title, background color, size, and setting the 'tracer' which tells the window to not update.
window = turtle.Screen()
window.title("Python Pong by Chip Brommer")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Starting Scores
score_a = 0
score_b = 0

# Left Paddle - Creating the left paddle: giving it shape, size, and setting its location
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("black")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-360, 0)

# Right Paddle - Creating the right paddle: giving it shape, size, and setting its location
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("black")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(360, 0)

# Pong Ball - Creating the ball: giving it shape, size, and setting its location to center
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2     #every time ball moves, it moves over two pixels at a time.
ball.dy = 2     #every time ball moves, it moves up two pixels at a time.

#   Score Board
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,260)
scoreboard.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "bold"))

# End Game
endgame = turtle.Turtle()
endgame.speed(0)
endgame.color("black")
endgame.penup()
endgame.hideturtle()
endgame.goto(0,0)

# Restart or Close
restart = turtle.Turtle()
restart.speed(0)
restart.color("black")
restart.penup()
restart.hideturtle()
restart.goto(0,-60)

# Functions
def left_paddle_up():
    y = left_paddle.ycor()  # getting the paddles y co-ordinate
    y += 20                 # +20 so paddle moves up 15 pixels at a time.
    left_paddle.sety(y)     #re-setting the y c-ordinate for paddle.

def left_paddle_down():
    y = left_paddle.ycor()  # getting the paddles y co-ordinate
    y -= 20                 # -20 so paddle moves down 15 pixels at a time.
    left_paddle.sety(y)     #re-setting the y c-ordinate for paddle.

def right_paddle_up():
    y = right_paddle.ycor()  # getting the paddles y co-ordinate
    y += 20                 # +20 so paddle moves up 15 pixels at a time.
    right_paddle.sety(y)     #re-setting the y c-ordinate for paddle.

def right_paddle_down():
    y = right_paddle.ycor()  # getting the paddles y co-ordinate
    y -= 20                 # -20 so paddle moves down 15 pixels at a time.
    right_paddle.sety(y)     #re-setting the y c-ordinate for paddle.


def game_over():
    if score_a == 5:
        left_paddle.hideturtle()
        right_paddle.hideturtle()
        ball.goto(0,0)          # setting ball back to center
        ball.dx = 0             # stopping ball
        ball.dy = 0
        ball.hideturtle()       # hiding ball
        endgame.write("Player A Wins!", align="center", font=("Courier", 48, "bold"))
    #restart.write("Press 'R' to restart or 'X' to close!", align="center", font=("Courier", 24, "bold"))
    elif score_b == 5:
        left_paddle.hideturtle()    # hiding left paddle
        right_paddle.hideturtle()   # hiding right paddle
        ball.goto(0,0)          # setting ball back to center
        ball.dx = 0             # stopping ball
        ball.dy = 0
        ball.hideturtle()       # hiding ball
        endgame.write("Player B Wins!", align="center", font=("Courier", 48, "bold"))
#restart.write("Press 'R' to restart or 'X' to close!", align="center", font=("Courier", 24, "bold"))

# Keyboard Bindings
window.listen()
window.onkeypress(left_paddle_up, "q")      # setting the up movement to keyboard 'q'
window.onkeypress(left_paddle_down, "a")    # setting the down movement to keyboard 'a'
window.onkeypress(right_paddle_up, "o")     # setting the up movement to keyboard 'o'
window.onkeypress(right_paddle_down, "l")   # setting the down movement to keyboard 'l'


while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Setting borders
    if ball.ycor() > 290:       # 290 comes from splitting the ball and height in half: 600/2 - 20/2 = 290
        ball.sety(290)
        ball.dy *= -1           # if ball hits border, changes direction to opp. way by multipling value by -1
        os.system("afplay bounce.wav&")
    
    if ball.ycor() < -290:       # -290 comes from splitting the ball and height in half: 600/2 - 20/2 = 290
        ball.sety(-290)
        ball.dy *= -1           # if ball hits border, changes direction to opp. way by multipling value by -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 398:       # 398 comes from the width of screen and moving in 2 pixels. Means ball has                                 passed paddle.
        score_a += 1            # adding point to player A
        ball.goto(0,0)          # setting ball back to center
        ball.dx *= -1           # reversing ball direction
        scoreboard.clear()      # clearing the scoreboard for the updated point
        scoreboard.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        game_over()

    if ball.xcor() < -398:       # 398 comes from the width of screen and moving in 2 pixels. Means ball has                                 passed paddle.
        score_b += 1            # adding point to player B
        ball.goto(0,0)          # setting ball back to center
        ball.dx *= -1           # reversing ball direction
        scoreboard.clear()      # clearing the scoreboard for the updated point
        scoreboard.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        game_over()
    

    # Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.dx *= -1                       #reversing ball direction
        os.system("afplay bounce.wav&")     #playing bounce sound

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.dx *= -1                       #reversing ball direction
        os.system("afplay bounce.wav&")     #playing bounce sound
