import turtle
from turtle import*
a = turtle.Screen()
a.bgcolor("lightgreen")
b = turtle.Turtle()
b.color("hotpink")

def drawfive_star():    
    for i in range(5):
        forward(100)
        right(144)
    

for i in range(5):
    drawfive_star()
    up()
    forward(350)
    right(144)
    down()
