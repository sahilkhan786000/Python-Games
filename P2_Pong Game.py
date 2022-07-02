import turtle


wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("Black")
wn.setup(800,600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.up()
paddle_a.goto(-350,0)


# Paddle B


paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.up()
paddle_b.goto(350,0)


# Ball

ball = turtle.Turtle()
ball.speed(-2)
ball.shape("circle")
ball.color("red")
ball.up()
ball.goto(0,0)
ball.dx = 0.7
ball.dy = -0.7

ball1 = turtle.Turtle()
ball1.speed(-2)
ball1.shape("circle")
ball1.color("blue")
ball1.up()
ball1.goto(0,0)
ball1.dx = -0.7
ball1.dy = -0.7




#  Pen
pen = turtle.Turtle()
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0  Player B : 0", align="center", font=("Courier",24,"normal"))







# function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y = y-20
    paddle_a.sety(y)



def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y = y-20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "a")
wn.onkeypress(paddle_a_down, "b")
wn.onkeypress(paddle_b_up, "c")
wn.onkeypress(paddle_b_down, "d")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ball1.setx(ball1.xcor() + ball1.dx)
    ball1.sety(ball1.ycor() + ball1.dy)

    # Border Checking
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A :{}  Player B : {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A :{}  Player B : {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and ( ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1



    if ball1.ycor() > 290 :
        ball1.sety(290)
        ball1.dy *= -1


    if ball1.ycor() < -290:
        ball1.sety(290)
        ball1.dy *= -1


    if ball1.xcor() > 390:
        ball1.goto(0,0)
        ball1.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A :{}  Player B : {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball1.xcor() < -390:
        ball1.goto(0,0)
        ball1.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A :{}  Player B : {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and Ball Collision
    if (ball1.xcor() > 340 and ball1.xcor() < 350 ) and (ball1.ycor() < paddle_b.ycor() +40 and ball1.ycor() > paddle_b.ycor() -40):
        ball1.setx(340)
        ball1.dx *= -1


    if (ball1.xcor() < -340 and ball1.xcor() > -350) and ( ball1.ycor() < paddle_a.ycor() + 40 and ball1.ycor() > paddle_a.ycor() - 40):
        ball1.setx(-340)
        ball1.dx *= -1






    # AI Player
    if ball.xcor() > ball1.xcor():

     if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor()-ball.ycor()) > 10:
        paddle_b_up()

     elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor()-ball.ycor()) > 10:
        paddle_b_down()

    else:
     if paddle_b.ycor() < ball1.ycor() and abs(paddle_b.ycor() - ball1.ycor()) > 10:
            paddle_b_up()

     elif paddle_b.ycor() > ball1.ycor() and abs(paddle_b.ycor() - ball1.ycor()) > 10:
            paddle_b_down()

