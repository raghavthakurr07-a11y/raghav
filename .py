import turtle
import time

screen = turtle.Screen()
screen.bgcolor("WHITE")
screen.title("Happy Birthday")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(1)
pen.color("BLACK")
pen.penup()

# Happy Birthday Text
pen.goto(0, 100)
pen.write("🎉 HAPPY BIRTHDAY 🎉 PRERNA ❤️", align="center",
          font=("Arial", 24, "bold"))

time.sleep(1)

# Balloons
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

for i in range(6):
    pen.goto(-180 + i * 70, -50)
    pen.color(colors[i])

    # Balloon
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

    # String
    pen.right(90)
    pen.forward(60)
    pen.backward(60)
    pen.left(90)

# Moving Star
star = turtle.Turtle()
star.shape("circle")
star.color("gold")
star.penup()
star.speed(1)

for _ in range(2):
    star.goto(-250, 180)
    star.goto(250, 180)

pen.goto(0, -150)
pen.color("BLACK")
pen.write("Have a Wonderful Day! 🎂",
          align="center",
          font=("Arial", 18, "bold"))

turtle.done()
