# hexagon() -- this should have the same parameters as square and triangle but should draw a hexagon.

import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

def hexagon (t, x, y, w, color, sidelen):
    #set the location, color, and width
    t.penup()
    t.goto(x, y)
    t.width(w)
    t.color(color)
    t.pendown()
    #to draw a hexagon
    for i in range(6):
        t.forward(sidelen)
        t.right(60)

hexagon(crush, 0, 0, 1, "green", 50)


# ngon(t,numsides,x,y,color,width,sidelen) - this will draw a regular ngon with numsides sides.
numsides = int(input("How many sides are in your regular ngon?"))

def ngon (t, numsides, x, y, color, width, sidelen):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.width(width)
    t.pendown()
    #to draw a ngon with numsides 
    for i in range(numsides):
        t.pendown()
        t.forward(sidelen)
        t.right(360/numsides)

ngon(crush, numsides, 0, 0, "green", 1, 50)






