from turtle import *
import random

class star:
    pass

speed(speed='fastest')

# Caleb Mburu
# Overlapping Stars
# Python
# My project draws stars with random colors. It takes 3 parameters
# at the bottom of the code that the user can manipulate.
# The first is the number of stars, second is the exterior angle of the star, and
# third is the angle the stars rotates.

def draw(num_stars, x, angle):
    # loop for number of stars
    for i in range(num_stars):

        colormode(255)

        # random integers to generate random rgb values
        color_1 = random.randint(0, 255)
        color_2 = random.randint(0, 255)
        color_3 = random.randint(0, 255)

        # setting outline and fill colour
        pencolor(color_1, color_2, color_3)
        fillcolor(color_1, color_2, color_3)

        # fills the star
        begin_fill()

        # loop for drawing each star
        for j in range(7):
            forward(7 * num_stars - 7 * i)
            left(x)
            forward(7 * num_stars - 7 * i)
            left(72-x)

        # filling complete
        end_fill()

        # rotating for the next star
        rt(angle)


# user can set the parameters
num_stars = 25  # number of stars
x = 150  # exterior angle of each star
angle = 44  # angle of rotation for the spiral

draw(num_stars, x, angle)
