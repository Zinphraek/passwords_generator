from turtle import *
speed(5)

left(90)
forward(220)
right(90)
forward(50)
for i in range(20):
    right(9)
    forward(10)
forward(40)
back(50)
left(120)
forward(105)

hideturtle()
getscreen().getcanvas().postscript(file='output.ps')
