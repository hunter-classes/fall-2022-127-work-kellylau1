import turtle

def sample_function(): 
  print("This is a function")
  print("It can be used multiple times")



  

wn = turtle.Screen()

crush = turtle.Turtle()



#draw a square 
for i in range(4):
  crush.forward(50)
  crush.right(90)


#create a second turtle into the variable squirt and make a squirt draw a triangle 

squirt = turtle.Turtle()
squirt.up()
squirt.goto(100,100)
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

for number in range(5,10): 
  print(number)

print("---------------------")

for name in ["able", "baker", "charlie"]:
  print(name)
  print(name.upper())

print("The loop is done")


sample_function()

wn.exitonclick()
wn.mainloop()