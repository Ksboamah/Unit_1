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
def makesquare(size):
    for x in range(4):
        turtle.left(90)
        turtle.forward(size)

for x in range(3):
    makesquare(50)
    turtle.left(20)

turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()

def makehouse(size, color, color2):
    turtle.color(color)
    turtle.begin_fill()
    makesquare(size)
    turtle.end_fill()
    turtle.color(color2)
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.end_fill()

turtle.penup()
turtle.goto(600,-300)
turtle.pendown()

turtle.seth(0)

for x in range(4):
    makehouse(100,"red","red")
    turtle.penup()
    turtle.left(50)
    turtle.forward(300)
    turtle.pendown()

turtle.penup()
turtle.goto(-500,300)
turtle.pendown()

turtle.seth(0)
for x in range(4):
    makehouse(100,"red","blue")
    turtle.penup()
    turtle.right(50)
    turtle.forward(300)
    turtle.pendown()

turtle.penup()
turtle.goto(-700,300)
turtle.pendown()

turtle.seth(0)
for x in range(4):
    makehouse(50,"yellow","pink")
    turtle.penup()
    turtle.right(50)
    turtle.forward(300)
    turtle.pendown()

turtle.exitonclick()