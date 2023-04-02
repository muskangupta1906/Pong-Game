import turtle
import winsound

# Game Window
s = turtle.Screen()
s.title("Muskan's First Python Game")
s.bgcolor('#87CEEB')
s.setup(width=800, height=600)
s.tracer(0)

# Ball
ball = turtle.Turtle()
ball.color("black")
ball.speed(0)
ball.shape("square")
ball.penup()
ball.goto(0,0)
ball.dx = 0.20
ball.dy = 0.20

# Score
score_a = 0
score_b = 0

#Pen
pen = turtle.Turtle()
pen.color("Purple")
pen.hideturtle()
pen.penup()
pen.goto(0,250)
pen.write("Player A : 0 | Player B : 0", align = "center", font = ("Courier", 22 , "normal"))

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color('#A020F0')
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(5,1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color('#A020F0')
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(5,1)

# Functions

def paddle_a_up():
    y = paddle_a.ycor()
    y+= 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y-= 20
    paddle_b.sety(y)

# Keyboard Binding

s.listen()
s.onkeypress(paddle_a_up,"w")
s.onkeypress(paddle_a_down,"s")
s.onkeypress(paddle_b_up,"Up")
s.onkeypress(paddle_b_down,"Down")


    
#Main game loop
while True:
    s.update()
    
    # Ball Bounce
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor()>390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))
        ball.goto(0,0)
        ball.dx *= -1 
        winsound.PlaySound("negative_beeps.mp3", winsound.SND_ASYNC)
    

    if ball.xcor()<-390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))
        ball.goto(0,0)
        ball.dx *= -1 
        winsound.PlaySound("negative_beeps.mp3", winsound.SND_ASYNC)

    # ball and paddle collision

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor() + 50 and ball.ycor()>paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor() + 50 and ball.ycor()>paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # border conditions on paddles
    if paddle_b.ycor()>= 300:
        paddle_b.sety(-300) 
    elif paddle_b.ycor()<= -300:
        paddle_b.sety(300) 

    if paddle_a.ycor()>= 300:
        paddle_a.sety(-300) 
    elif paddle_a.ycor()<= -300:
        paddle_a.sety(300) 

s.exitonclick()
