#5 Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)

def max():
  max.sort()
  return max[-1]
print(max[1,5,3])





#7 Write a function to count how many odd numbers are in a list.

def odd(list): 
  result = []
  for num in list: 
    if num % != 0: 
      num.append(result)

  for num in result: 
    result = len(result)
  return result 


list = [1, 2 , 3]
print(odd(list))





#8 Sum up all the even numbers in a list.

def sum(list): 
  result = []
  for num in list: 
    if num % 2 == 0: 
      num.append(result)

  for num in result: 
    sum = 0 
    sum = sum + num 
  return result

list = [ 1, 2, 3 , 4]

print(sum(list))