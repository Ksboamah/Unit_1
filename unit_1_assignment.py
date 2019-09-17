# Kwame Sakyi Boamah created this on Tuesday, September 17th, 2019
# This code creates different colored octagons on different parts of the page


import turtle
def makeoctagon(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(8):

        turtle.forward(size)
        turtle.left(45)
    turtle.end_fill()

# Makes a red octagon
makeoctagon(50, "red")

def goto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

goto(100,100)

# Makes a blue octagon
makeoctagon(50,"blue")

goto(200,200)

# Makes a yellow octagon
makeoctagon(50, "yellow")

goto(-100,-100)

# Makes a pink octagon
makeoctagon(50, "pink")

turtle.exitonclick()
