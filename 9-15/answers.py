#7 - Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

number = int(input("Enter a number: "))
def is_even(n):
    even = n%2
    if even == 0:
        return True
    else:
        return False

is_even(number)

#8 - Now write the function is_odd(n) that returns True when n is odd and False otherwise.

number = int(input("Enter a number: "))

def is_even(n):
    even = n%2
    return even
def is_odd(even):
    if even != 0 or even > 0:
        return True
    else:
        return False

is_even(number)

#10 - Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

a = int(input("Length of a = "))
b = int(input("Length of b = "))
c = int(input("Length of c = "))
hypotenuse = c**2

def is_rightangled(a, b, c):
  pythagorean = a**2 + b**2 == hypotenuse 
  return pythagorean 

  if pythagorean < hypotenuse or pythagorean > hypotenuse:
    return False 
  else: 
    return True 
    
is_rightangled(a,b,c)

#11 - Extend the above program so that the sides can be given to the function in any order.

def is_rightangled(a, b, c):
  pythagorean1 = a**2 + b**2 == c**2 
  return pythagorean1
  pythagorean2 = a**2 + c**2 == b**2
  return pythagorean2
  pythagorean3 = b**2 + c**2 == a**2
  return pythagorean3

  pythagorean = [pythagorean1, pythagorean2, pythagorean3]

  for x in pythagorean:
    if x < pythagorean.rhs or x > pythagorean.rhs:
      return False 
  else: 
    return True 
    
is_rightangled(a,b,c)


# #String-1 hello_name
def hello_name(name):
    return "hello", name + "!"


# #String-1 make_out_world
def make_out_word(out, word):
    return out[:2] + word + out[2:]


# #String-1 first_two
def first_two(str):
  return str[:2]