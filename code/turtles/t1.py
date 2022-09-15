#STRINGS------------------------------------

s1 = "Hello World"
s2 = 'another\nstring'

s3 = """
This is a multiline string
we use the triple quotes
for those
"""

s4 = s1+s1 # string catenation

print(s4)
print(s1*3)
print(3*s1)

print(len(s1))
print(len("abcde"))

# isolate the world from s1
# first find the space
space_location = s1.find(" ")
print(space_location)
# pull out from 6 (one after the space) until the end
#s5 = s1[space_location+1:len(s1)]
s5 = s1[space_location+1:] # nothing after the : means go to the end
print(s5)









#----------------------------------------

import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

squirt = turtle.Turtle()

def sample_function():
    print("This is a function")
    print("It can be used multiple times")






def square(t, x, y, w, color, sidelen):
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

square(crush, 0, 0, 1, "green", 50)
square(squirt, 100, 100, 5,"red", 80)
square(crush, -50, 30, 3, "yellow", 100)



#create a second turtle into the variable squirt and make a squirt draw a triangle
squirt.up()
squirt.goto(100, 100)
squirt.down()
squirt.color("red")
squirt.width(5)


for i in range(3):
    squirt.forward(50)
    squirt.left(120)

#--------------------------------

for i in range(4):
    print(i)

print("---------------------")

for number in range(5, 10):
    print(number)

print("---------------------")

for name in ["able", "baker", "charlie"]:
    print(name)
    print(name.upper())

print("The loop is done")

sample_function()

wn.exitonclick()
wn.mainloop()
