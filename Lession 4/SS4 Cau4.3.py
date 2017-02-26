import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("pink")
def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

draw_poly(tess,8,50)
