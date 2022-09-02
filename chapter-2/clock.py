#Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off.

current_time = int(input("What is the current time? "))
wait_time = int(input("How many hours do you want to wait for the alarm? "))

add = current_time + wait_time
if add and current_time <= 12 :
  print("The alarm will go off at", add ,"PM.")
else: 
  time = (current_time - 12)
  divide = (wait_time // 24)
  hours = int(50 - (24*divide))
  alarm = time + hours
  print("The alarm will go off at", alarm , "PM.")






