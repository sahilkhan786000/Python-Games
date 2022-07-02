import math
import turtle
import random

wn = turtle.Turtle()
turtle.bgcolor("black")
turtle.title("Maze Game")
turtle.setup(600,600)

#Registere shapes :


# Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


# class Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        #Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls :
            self.goto(move_to_x, move_to_y)


    def go_down(self):
        # Calculate the spot to move to
        move_to_x =self.xcor()
        move_to_y = self.ycor() - 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_left(self):
        # Calculate the spot to move to
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Calculate the spot to move to
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def is_collision(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance <  5:
            return True
        else :
            return False

class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold =100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx=0
            dy=24

        elif self.direction == "down":
            dx = 0
            dy = -24

        elif self.direction == "left":
            dx = -24
            dy = 0

        elif self.direction == "right":
            dx = 24
            dy = 0

        else :
            dx =0
            dy =0

        #Check if player is close
        #If so, go in that direction

        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction = "left"

            elif player.xcor()>self.xcor():
                self.direction = "right"

            elif player.ycor() < self.ycor():
                self.direction = "down"

            elif player.ycor() > self.ycor():
                self.direction = "up"

        # calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy


        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else :
            #choose a different direction
            self.direction =  random.choice(["up", "down", "left", "right"])

        # Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100,300,))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()

        distance = math.sqrt((a**2) + (b**2))
        if distance < 75 :
            return True
        else:
            return False




    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

# Define first level
levels = [""]


#Create levels list
level_1 =["XXXXXXXXXXXXXXXXXXXXXXXXX",
          "XP XXXXXXX          XXXXX",
          "X  XXXXXXX  XXXXXX  XXXXX",
          "X       XX  XXXXXX  XXXXX",
          "X       XX  XXX        XX",
          "XXXXXX  XX  XXX        XX",
          "XXXXXX  XX  XXXXXX  XXXXX",
          "XXXXXX  XX    EXXX  XXXXX",
          "X  XXX        XXXX  XXXXX",
          "X  XXX  EXXXXXXXXXXXXXXXX",
          "X         TXXXXXXXXXXXXXX",
          "X                XXXXXXXX",
          "XXXXXXXXXXXX     XXXXX  X",
          "XXXXXXXXXXXXXXE  XXXXX  X",
          "XXX  XXXXXXXXXX         X",
          "XXX                     X",
          "XXX         XXXXXXXXXXXXX",
          "XXXXXXXXXX  XXXXXXXXXXXXX",
          "XXXXXXXXXX              X",
          "XX   XXXXX              X",
          "XX  XXXXXXXXXXXXXX  XXXXX",
          "XX   XXXXXXXXXXXXX  XXXXX",
          "XX          XXXX        X",
          "XXXX                    X",
          "XXXXXXXXXXXXXXXXXXXXXXXXX",
          ]

# Add a treasure list
treasures = []
enemies = []
# Add maze to mazes list
levels.append(level_1)
#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get character at x,y coordinate
            #Note the order of y and x in the next line
            character = level[y][x]
            #calculate the screen x,y coordinates
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            # check if it is an X(representing a wall)
            if character =='X':
                pen.goto(screen_x, screen_y)
                pen.stamp()
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))


            # check if it is an P(representing a player)
            if character == 'P':
                player.goto(screen_x, screen_y)

            # check if it is a T (representing treasure)
            if character == 'T':
                treasures.append(Treasure(screen_x, screen_y))

            # check if it is a T (representing treasure)
            if character == 'E':
                enemies.append(Enemy(screen_x, screen_y))

#create class instance
pen = Pen()
player = Player()


# Create wall coordinates list
walls = []

#set up  the level
setup_maze(levels[1])

#keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# Turn off screen updates
turtle.tracer(0)

#Start moving enemies
for enemy in enemies :
    turtle.ontimer(enemy.move, t=250)


# Main Gme loop
while True:
    #Check for player collision with treasure
    #Iterate through treasure list
    for treasure in treasures :
        if player.is_collision(treasure):
            #Add the treasure gold to the player gold
            player.gold += treasure.gold
            print("player Gold : {}".format(player.gold))
            #Destroy the treasure
            treasure.destroy()
            #Remove the treasure from the treasures list
            treasures.remove(treasure)

    for enemy in enemies :
        if player.is_collision(enemy):
            print("Player dies : ")








# Update screen
    turtle.update()

turtle.mainloop()