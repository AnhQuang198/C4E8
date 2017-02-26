import turtle

def drawSpiral(t, sq):
    length = 1
    for i in range(84):
        t.forward(length)
        t.left(sq)
        length = length + 2


a = turtle.Screen()
a.bgcolor("lightgreen")

b = turtle.Turtle() 
b.color('blue')
b.penup()
b.backward(110)
b.pendown()
drawSpiral(b, 90)
speed(-1)


