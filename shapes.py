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
turtle.forward(200)

turtle.pendown()
turtle.left(70)
turtle.forward(100)
turtle.right(135)
turtle.forward(100)
turtle.right(150)
turtle.forward(100)


turtle.exitonclick()