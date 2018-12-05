# Draws a dodecadon with the colour of each sector alternating red and blue.
#
# Written by Kun Zhang

from turtle import *
from math import *

angle = 22.5
edge_length_yellow = 100/cos(angle*pi/180)
edge_length_spur = 180
speed(100)

vertices_yellow = []
vertices_spurs = []

penup()
#8 points
for i in range(16):
    if i%2 == 0:
        right(i * angle)
        forward(edge_length_yellow)
        vertices_yellow.append(pos())
    else:
        right(i * angle)
        forward(edge_length_spur)
        vertices_spurs.append(pos())
    home()

def draw_triangle(i, colour):
    color(colour)
    begin_fill()
    goto(vertices_yellow[i])
    goto(vertices_spurs[i])
    if i==7:
        goto(vertices_yellow[0])
    else:
        goto(vertices_yellow[i + 1])
    end_fill()

def draw_yellow(colour='yellow'):
    color(colour)
    begin_fill()
    for i in range(8):
        goto(vertices_yellow[i])
    end_fill()

goto(vertices_yellow[0])
pendown()
for i in range(8):
    # If i is odd because the division of i by 2 yields a remainder of 1
    # then make colour 'red'; otherwise make it 'blue'.
    if i % 2:
        colour = 'red'
    else:
        colour = 'blue'
    draw_triangle(i, colour)

draw_yellow()


while(1):
    pass






    
    

