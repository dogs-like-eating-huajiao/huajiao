import turtle
turtle.screensize(400,400,"white")
turtle.pencolor("red")
turtle.speed(0)
from math import *#应用时不用前缀
r=100
t=0
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("pink")
for t in range(360):
    t=t/360*2*pi
    x=2*r*(sin(t)-sin(2*t)/2)
    y=2*r*(cos(t)-cos(2*t)/2)
    turtle.goto(x,y)
turtle.end_fill()
turtle.done()