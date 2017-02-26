import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

a = turtle.Screen()
a.bgcolor("lightgreen")

b = turtle.Turtle()
b.color('hotpink')
b.pensize(3)

for i in range(5):
    drawSquare(b, 20)
    b.penup()
    b.forward(40)
    b.pendown()

a.exitonclick()
