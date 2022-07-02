
import time
import turtle
import random

delay = 0.1

# Score
score = 0
high_score = 0




# set up screen
wn = turtle.Screen()
wn.title("Snake mania")
wn.setup(600, 600)
wn.bgcolor("green")
wn.tracer(0) # Turn off Screen update


# Snake Head
head= turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("black")
head.penup()
head.goto(0,0)







head.direction='right'

# snake food

food= turtle.Turtle()
food.speed(0)
food.pensize(1)
food.shape('circle')
food.color("red")
food.penup()
food.goto(0,30)
food.direction='right'


segments = []


pen= turtle.Turtle()
pen.speed(0)
pen.pensize(1)
pen.shape('circle')
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score : 0", align = "center", font = ("Courier",24,"normal"))



# functions

def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'

# functions
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)



# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# main Game loop
while True:
    wn.update()

 # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
        head.goto(0, 0)
        time.sleep(0.005)




        # hide the segments
        for segment in segments :
            segment.goto(1000,1000)

        # clear the segment list
        segments.clear()

        # Reset the score
        score =  0

        pen.clear()
        pen.write("Score : {}  High Score: {} ".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))




    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to random spot
        x = random.randint(-290 , 290)
        y = random.randint(-290 , 290)
        food.goto(x , y)


        #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


        #shortens the delay
        delay -= 0.001


        # Increase Score
        score = score +10

        if score > high_score :
            high_score = score
        pen.clear()
        pen.write("Score : {}  High Score: {} ".format(score, high_score), align="center", font = ("Courier",24,"normal"))



# Move the end segment in reverese order

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

# Move segment 0 to where th head is

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()
#check for the head collision  with th body segments
    for segment in segments:

        if segment.distance(head) < 20 :

            time.sleep(0.005)
            head.goto(0,0)
            head.direction = "stop"

            # hide the segment list
            for segment in segments:
                segment.goto(1000,1000)

            # Clear the segments list
            segments.clear()

    time.sleep(delay)

turtle.mainloop()