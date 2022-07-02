'''
# https://christianthompson.com
# Twitter: @tokyoedtech

# Welcome to my live coding session
# Topic: TETRIS Part 3

# OS: Ubuntu Linux 19.04
# Programming Editor: Geany

# TETRIS Using Python 3 and the Turtle Module

import turtle
import time
import random

wn = turtle.Screen()
wn.title("TETRIS by @TokyoEdTech")
wn.bgcolor("NavajoWhite2")
wn.setup(width=600, height=800)
wn.tracer(0)

delay = 0.1


class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)

        # Block Shape
        square = [[1, 1],
                  [1, 1]]

        horizontal_line = [[1, 1, 1, 1]]

        vertical_line = [[1],
                         [1],
                         [1],
                         [1]]

        left_l = [[1, 0, 0, 0],
                  [1, 1, 1, 1]]

        right_l = [[0, 0, 0, 1],
                   [1, 1, 1, 1]]

        left_s = [[1, 1, 0],
                  [0, 1, 1]]

        right_s = [[0, 1, 1],
                   [1, 1, 0]]

        t = [[0, 1, 0],
             [1, 1, 1]]

        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]

        # Choose a random shape each time
        self.shape = random.choice(shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])

        # print(self.height, self.width)

    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1

    def move_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if (self.shape[y][x] == 1):
                    grid[self.y + y][self.x + x] = self.color

    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if (self.shape[y][x] == 1):
                    grid[self.y + y][self.x + x] = 0

    def can_move(self, grid):
        result = True
        for x in range(self.width):
            # Check if bottom is a 1
            if (self.shape[self.height - 1][x] == 1):
                if (grid[self.y + self.height][self.x + x] != 0):
                    result = False
        return result

    def rotate(self, grid):
        # First erase_shape
        self.erase_shape(grid)
        rotated_shape = []
        for x in range(len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape) - 1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)

        right_side = self.x + len(rotated_shape[0])
        if right_side < len(grid[0]):
            self.shape = rotated_shape
            # Update the height and width
            self.height = len(self.shape)
            self.width = len(self.shape[0])


grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Create the drawing pen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)


def draw_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110

    colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()


def check_grid(grid):
    # Check if each row is full
    y = 23
    while y > 0:
        is_full = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
        if is_full:
            global score
            score += 10
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y - 1][copy_x]


def draw_score(pen, score):
    pen.color("blue")
    pen.hideturtle()
    pen.goto(-75, 350)
    pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))


# Create the basic shape for the start of the game
shape = Shape()

# Put the shape in the grid
grid[shape.y][shape.x] = shape.color

# Draw the initial grid
# draw_grid(pen, grid)


wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "a")
wn.onkeypress(lambda: shape.move_right(grid), "d")
wn.onkeypress(lambda: shape.rotate(grid), "space")

# Set the score to 0
score = 0

draw_score(pen, score)

# Main game loop
while True:
    wn.update()

    # Move the shape
    # Open Row
    # Check for the bottom
    if shape.y == 23 - shape.height + 1:
        shape = Shape()
        check_grid(grid)
    # Check for collision with next row
    elif shape.can_move(grid):
        # Erase the current shape
        shape.erase_shape(grid)

        # Move the shape by 1
        shape.y += 1

        # Draw the shape again
        shape.draw_shape(grid)

    else:
        shape = Shape()
        check_grid(grid)

    # Draw the screen
    draw_grid(pen, grid)
    draw_score(pen, score)

    time.sleep(delay)

wn.mainloop()
'''

# SPGL Game Demo by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
#
# How to Play
# Navigate using the arrow keys
# Green objects are worth 10 points
# Yellow objects are worth 5 points
# Red objects are worth -10 points

#Import SPGL
from spgl import *
import random

# Create Classes
class Player(Sprite):
    def __init__(self, shape, color, x, y):
        Sprite.__init__(self, shape, color, x, y)
        self.speed = 3
        self.score = 0

    def tick(self):
        self.move()

    def move(self):
        self.fd(self.speed)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

        if self.xcor() < -game.SCREEN_WIDTH /2 :
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())

        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)

    def rotate_left(self):
        self.lt(30)

    def rotate_right(self):
        self.rt(30)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1
        if self.speed < 0:
            self.speed = 0

class Orb(Sprite):
    def __init__(self, shape, color, x, y):
        Sprite.__init__(self, shape, color, x, y)
        self.speed = 2
        self.setheading(random.randint(0,360))
        self.turn = 0

    def tick(self):
        self.move()
        if random.randint(0, 100) < 5:
            self.clear()

    def move(self):
        self.rt(random.randint(-10, 10))
        self.fd(self.speed)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

        if self.xcor() < -game.SCREEN_WIDTH / 2:
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())

        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)

# Initial Game setup
game = Game(800, 600, "black", "SPGL Game Demo by /u/wynand1004 AKA @TokyoEdTech", 5)

# Game attributes
game.highscore = 0

# Load high score
highscore = game.load_data("highscore")
if highscore:
    game.highscore = highscore
else:
    game.highscore = 0

# Create Sprites
# Create Player
player = Player("triangle", "white", -400, 0)

# Create Orbs
for i in range(100):
    color = random.choice(["red", "yellow", "green"])
    shape = random.choice(["circle", "square", "triangle", "arrow"])
    orb = Orb(shape, color, 0, 0)
    speed = random.randint(1, 5)
    orb.speed = speed

# Create Labels
score_label = Label("Score: 0 Highscore: {}".format(game.highscore), "white", -380, 280)

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(KEY_UP, player.accelerate)
game.set_keyboard_binding(KEY_DOWN, player.decelerate)
game.set_keyboard_binding(KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(KEY_RIGHT, player.rotate_right)
game.set_keyboard_binding(KEY_ESCAPE, game.exit)

while True:
    # Call the game tick method
    game.tick()

    # Put your game logic here
    for sprite in game.sprites:
        # Check collisions with Orbs
        if sprite.state and isinstance(sprite, Orb):
            if game.is_collision(sprite, player):
                game.play_sound("collision.wav")
                sprite.destroy()
                # Update Score
                if sprite.pencolor() == "red":
                    player.score -= 10
                if sprite.pencolor() == "green":
                    player.score += 10
                if sprite.pencolor() == "yellow":
                    player.score += 5

                # Update High Score
                if player.score > game.highscore:
                    game.highscore = player.score
                    game.save_data("highscore", game.highscore)

    # Update the Game Score, High Score, and Player Speed
    speed_string = "-" * int(player.speed)
    score_label.update("Score: {} High Score: {} Speed: {}".format(player.score, game.highscore, speed_string))

    # Show game info in terminal
    game.clear_terminal_screen()
    game.print_game_info()
