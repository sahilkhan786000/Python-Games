import os
import random
import time

# Import Turtle Module
import turtle

# Required by MacOSX to show the window
turtle.fd(0)
turtle.setup(700, 700)

# Set the animations speed to the maximum
turtle.speed(0)
# Change the Background color
turtle.bgcolor("black")

turtle.bgpic("s.gif")
# Hie the default turtle
turtle.ht()
# this saves memory
turtle.setundobuffer(1)

# this speed up drawing
turtle.tracer(0)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)

        self.speed = 1

    def move(self):
        self.fd(self.speed)

        # Boundar detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
                (self.xcor() <= (other.xcor() + 20)) and \
                (self.ycor() >= (other.ycor() - 20)) and \
                (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False


class Player(Sprite):

    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class Enemy(Sprite):

    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))


class Ally(Sprite):

    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)

        # Boundar detection
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)


class Missile(Sprite):

    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        Missile.shapesize(self, stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.speed)

        # Border check
        if self.xcor() < -290 or self.xcor() > 290 or self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"


class Game():

    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        # Draw Border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "Score : %s" % (self.score)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))


# Create game objects
game = Game()

# Draw a game border
game.draw_border()

# Show the game status
game.show_status()

# Create my sprites

player = Player("triangle", "white", 0, 0)
# enemy = Enemy("circle","red",-100,0)
missile = Missile("triangle", "yellow", 0, 0)
# ally = Ally("square", "blue", 100,0)

allies = []
for i in range(6):
    allies.append(Ally("square", "blue", 100, 0))

enemies = []
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))

# keyboard bindings

turtle.onkeypress(player.turn_left, "Left")
turtle.onkeypress(player.turn_right, "Right")
turtle.onkeypress(player.accelerate, "Up")
turtle.onkeypress(player.decelerate, "Down")
turtle.onkeypress(missile.fire, "space")
turtle.listen()

# Main game loop
while True:
    turtle.update()
    time.sleep(0.05)
    player.move()
    # enemy.move()
    missile.move()
    # ally.move()

    for ally in allies:
        ally.move()

        # Check for a collision between the mission and the ally
        if missile.is_collision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = "ready"
            # Increas the score
            game.score -= 50
            game.show_status()

    for enemy in enemies:
        enemy.move()

        # Check for collision with the player
        if player.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score -= 100
            game.show_status()


            # Check for a collision between the mission and the enemy
        if missile.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready"
            # Increas the score
            game.score += 100
            game.show_status()



delay = input("Press enter to finish. >")
turtle.mainloop()
