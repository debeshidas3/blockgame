# Import Required Modules
import time
import turtle
import random

# Set Up the Screen
screen=turtle.Screen()
screen.title("Blocking Game")
screen.bgcolor("#dab1f2")
screen.setup(width=600,height=600)
screen.tracer(0) # Turns off the screen updates for smoother animation

# Create the Paddle
paddle =turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("green")
paddle.shapesize(stretch_wid=1,stretch_len=5)
paddle.penup()
paddle.goto(0,-250)

# Create the Ball
ball=turtle.Turtle()         
ball.speed(0)
ball.shape("turtle")
ball.color("purple")
ball.shapesize(stretch_len=1,stretch_wid=2)
ball.penup()
ball.goto(0,100)
ball.dx=random .choice([-2,2])
ball.dy=-2

# Move the Paddle
def paddle_left():
    x=paddle.xcor()
    x-=20
    if x<-250:
        x=-250
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 250:
        x = 250
    paddle.setx(x)   
    
screen.listen()
screen.onkey(paddle_left, "Left")
screen.onkey(paddle_right, "Right")

while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    time.sleep(0.025)

    # Check for wall collisions (left and right)
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1  # Reverse the horizontal direction

    # Check for top collision
    if ball.ycor() > 290:
        ball.dy *= -1  # Reverse the vertical direction

    # Check for bottom collision (game over)
    if ball.ycor() < -290:
        ball.goto(0, 100)
        ball.dy = -2  # Reset ball's position and speed
        # You can add a game over message here or end the game

    # Check for paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1  # Bounce the ball back
