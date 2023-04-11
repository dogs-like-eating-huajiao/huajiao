import turtle
import random
turtle.pensize(1)
turtle.speed(0)
turtle.colormode(255)
def ploygons(x,y,z):
    red=random.randint(0,250)
    blue=random.randint(0,250)
    green=random.randint(0,250)
    turtle.penup()
    turtle.screensize(400,400,"black")
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(red,green,blue)
    turtle.pencolor(red,green,blue)
    k=180-(z-2)*180/z
    turtle.begin_fill()
    for i in range(z):
        turtle.fd(20)
        turtle.rt(k)
    turtle.end_fill()
for j in range(20):
    x=random.randint(-400,400)
    y=random.randint(-400,400)
    z=random.randint(4,10)
    ploygons(x,y,z)
turtle.done()