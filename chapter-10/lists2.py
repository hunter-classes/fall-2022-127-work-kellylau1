#Write a function called average that takes a list of numbers as a parameter and returns the average of the numbers.

def average(num):
  sum = 0 
  for i in num: 
    sum = sum + i 

  average = sum / len(num)
  return average

num = [3,4,5]
print("Average:", average(num))







def sum_of_squares(l):
  sum = 0
  for item in l:
      sum = sum + item*item
  return sum

l = [1 , 2 , 3]

print(sum_of_squares(l))