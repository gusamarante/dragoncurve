from turtle import Turtle, Screen, mainloop
from random import random

# L-system set up
START = "fx"
RULES = {'x':'x+yf+', 'y':'-fx-y', 'f':'f', '+':'+', '-':'-'}

LEVEL = 13

screen = Screen()
screen.tracer(False)

# turtle initialization
turtle = Turtle(visible=False)

sub_string = string = START

for _ in range(LEVEL):

    # make a random color
    turtle.pencolor(random(), random(), random())

    # apply the RULES from text to graphics
    for character in sub_string:
        if character == '+':
            turtle.right(90)
        elif character == '-':
            turtle.left(90)
        elif character == 'f':
            turtle.forward(5)

    screen.update()

    # make a new generation of the L-system
    full_string = "".join(RULES[character] for character in string)

    sub_string = full_string[len(string):]  # only the new information

    string = full_string  # the complete string for the next generation

screen.tracer(True)
turtle.hideturtle()

mainloop()
