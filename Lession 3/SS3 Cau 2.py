##1.
from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range (3,8):
    color(colors[i-3])
    for j in range (i):    
        forward(100)
        left(360/i)
##2.
from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(0,5):
    color(colors[i])
    begin_fill()
    for j in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
