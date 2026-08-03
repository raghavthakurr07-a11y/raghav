

"""import turtle
import colorsys
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Unique Spiral Animation")
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
h = 0
for i in range(360):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    pen.pencolor(color)
    pen.forward(i * 1.5)
    pen.right(59)
    h += 0.005
turtle.done()
import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spider Animation")

spider = turtle.Turtle()
spider.speed(0)
spider.color("white")
spider.pensize(2)

angle = 0

while True:
    spider.clear()
    spider.penup()
    spider.goto(0, 0)
    spider.pendown()

    # Spider body
    spider.begin_fill()
    spider.fillcolor("black")
    spider.circle(20)
    spider.end_fill()

    # Spider legs animation
    for i in range(8):
        spider.penup()
        spider.goto(0, 0)
        spider.setheading(i * 45 + math.sin(math.radians(angle)) * 20)
        spider.forward(20)
        spider.pendown()
        spider.forward(50)

    angle += 8
    screen.update()"""
    
#animation
"""import colorsys 
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(1)
n ,h=36,0
for i in range(200):
    c=colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    h += 1 / n
    t.forward(i)
    t.left(30)
    t.circle(i, 45)
    turtle.done  """
    
from turtle import * 
import colorsys

speed(0)
bgcolor("black")
h=0
for i in range(16):
    for j in range(18):
        c= colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h+=0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
        circle(40, 24)
        


            
            
    
    
    

