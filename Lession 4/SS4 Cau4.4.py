from turtle import *
bgcolor("lightgreen")
color("blue")
speed(-1)
def draw_pretty_pattern(n):
    for i in range(n):
        for j in range(4):
            forward(100)
            left(90)
        left(360/n)
draw_pretty_pattern(20)

