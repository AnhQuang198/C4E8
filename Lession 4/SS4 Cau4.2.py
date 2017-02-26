from turtle import *
bgcolor("green")
color("pink")
def hinhvuong(a, length, c):
    for i in range(a):
        for j in range(4):
            forward(length)
            left(90)
        penup()
        goto(-10*(i+1),-10*(i+1))
        length = length + 20
        pendown()

hinhvuong(4,20,3)
    
    
    
