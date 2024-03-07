#Beginner Project
#simple Python game 
import turtle

#Score
score_a=0
score_b=0

wn = turtle.Screen()
wn.title("Ping pong game by Rajath Kumar V")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Left Paddle 
Left_Paddle = turtle.Turtle()
Left_Paddle.speed(0)
Left_Paddle.shape("square")
Left_Paddle.color("white")
Left_Paddle.shapesize(stretch_wid=5,stretch_len=1)
Left_Paddle.penup()
Left_Paddle.goto(-350,0)

#Right Paddle 
right_Paddle = turtle.Turtle()
right_Paddle.speed(0)
right_Paddle.shape("square")
right_Paddle.color("white")
right_Paddle.shapesize(stretch_wid=5,stretch_len=1)
right_Paddle.penup()
right_Paddle.goto(350,0)

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 1
Ball.dy = -1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0 ", align="center", font=("Courier", 24, "normal"))

#Function
def Left_Paddle_up():
    y = Left_Paddle.ycor()
    y += 20
    Left_Paddle.sety(y)

def Left_Paddle_down():
    y = Left_Paddle.ycor()
    y -= 20
    Left_Paddle.sety(y)

def Right_Paddle_up():
    y = right_Paddle.ycor()
    y += 20
    right_Paddle.sety(y)

def Right_Paddle_down():
    y = right_Paddle.ycor()
    y -= 20
    right_Paddle.sety(y)

#keyboard Binding
wn.listen()
wn.onkeypress(Left_Paddle_up, "w")
wn.onkeypress(Left_Paddle_down, "s")
wn.onkeypress(Right_Paddle_up, "Up")
wn.onkeypress(Right_Paddle_down, "Down")

#Main Game Loop
while True:
    wn.update()

    #Move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #borderchecking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
               
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        
    #paddle and ball collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and ( Ball.ycor() < right_Paddle.ycor()+ 40 and Ball.ycor() > right_Paddle.ycor() - 40 ):
            Ball.setx(340)
            Ball.dx *= -1

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and ( Ball.ycor() < Left_Paddle.ycor()+ 40 and Ball.ycor() > Left_Paddle.ycor() - 40 ):
            Ball.setx(340)
            Ball.dx *= -1