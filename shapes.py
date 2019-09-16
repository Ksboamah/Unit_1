import turtle
turtle.speed(0)
turtle.forward(100)
turtle.left(135)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)

turtle.penup()
turtle.right(50)
turtle.forward(100)

turtle.pendown()
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(90)
turtle.forward(142)

turtle.penup()
turtle.forward(150)
turtle.pendown()

turtle.circle(50)

turtle.penup()
turtle.right(90)
turtle.forward(100)

turtle.pendown()
for x in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.forward(250)

turtle.pendown()
turtle.right(145)
turtle.forward(100)
turtle.right(145)
turtle.forward(100)
turtle.right(145)
turtle.forward(100)
turtle.right(145)
turtle.forward(100)
turtle.right(145)
turtle.forward(100)

turtle.penup()
turtle.goto(300,300)
turtle.pendown()

turtle.left(135)
def makesquare():
    for x in range(4):
        turtle.left(90)
        turtle.forward(100)

for x in range(3):
    makesquare()
    turtle.left(20)

turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()

def makehouse():
    turtle.color('red')
    turtle.begin_fill()
    makesquare()
    turtle.end_fill()
    turtle.color('blue')
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.end_fill()

turtle.penup()
turtle.goto(600,-300)
turtle.pendown()

turtle.seth(0)

for x in range(4):
    makehouse()
    turtle.penup()
    turtle.left(50)
    turtle.forward(300)
    turtle.pendown()


turtle.exitonclick()