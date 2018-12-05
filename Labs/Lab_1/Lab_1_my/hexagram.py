# Draws a hexagram with two colours
# Written by Kun Zhang for COMP9021

from turtle import *
from math import*

edge_length = 40
angle = 120

def teleport(distance):
    penup()      
    forward(distance)
    pendown()

def draw_tri(colour,degree):
	color(colour)
	for _ in range(3):
		right(degree)
		forward(edge_length)
		teleport(edge_length)
		forward(edge_length)
		right(degree)

draw_tri("red", 60)
right(90)
teleport(2*sqrt(3)*edge_length)
right(90)
draw_tri("blue", 120)

