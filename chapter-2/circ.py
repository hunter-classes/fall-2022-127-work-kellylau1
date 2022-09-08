#Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

radius = input("Enter the radius of the circle: ")
pi = int(3.14)
area = float(radius * (pi**2))
message = print("The area of the circle is", area)