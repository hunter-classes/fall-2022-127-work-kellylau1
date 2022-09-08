import turtle

wn = turtle.Screen()
greener = turtle.Turtle()
wn.bgcolor("light green")
greener.color("blue")
greener.shape("turtle")
greener.width(2)
greener.stamp()


greener.right(30)
greener.penup()

for i in range(11):
    greener.left(30)
    greener.goto(0,0)
    greener.forward(120)
    greener.pendown()
    greener.forward(10)
    greener.penup()
    greener.forward(20)
    greener.stamp()


wn.exitonclick()
wn.mainloop()