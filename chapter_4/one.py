# Write a program that prints We like Python's turtles! 100 times.

for i in range(101):
    print("We like Python's turtles!")



# hexagon() -- this should have the same parameters as square and triangle but should draw a hexagon.
# ngon(t,numsides,x,y,color,width,sidelen) - this will draw a regular ngon with numsides sides.


def hexagon (t, x, y, w, color, sidelen):
    #set the location, color, and width
    t.penup()
    t.goto(x, y)
    t.width(w)
    t.color(color)
    t.pendown()
    #to draw a square
    for i in range(4):
        t.forward(sidelen)
        t.right(90)

hexagon(crush, 0, 0, 1, "green", 50)