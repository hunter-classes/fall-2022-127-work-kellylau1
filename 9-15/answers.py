#7 - Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

number = int(input("Enter a number: "))
def is_even(n):
    return n%2 == 0  #this returns true or false 

is_even(number)

# #8 - Now write the function is_odd(n) that returns True when n is odd and False otherwise.

number = int(input("Enter a number: "))

def is_odd(n):
  return not(is_even(n))

is_odd(number)




#10 - Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

def is_rightangled(a, b, c):
  return a**2 + b**2 == c**2

print(is_rightangled(3,4,5))



#11 - Extend the above program so that the sides can be given to the function in any order.

def is_rightangled(a, b, c):
  return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2
    
print(is_rightangled(4,3,5))



# # #String-1 hello_name
def hello_name(name):
    return "Hello "+ name + "!"
print(hello_name("Kelly"))

# # #String-1 make_out_world
'''
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
'''

def make_out_word(out, word):
    return out[:2] + word + out[2:]

print(make_out_word("<<>>","kelly"))



'''
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

first_two('Hello') → 'He'
'''
# # #String-1 first_two
def first_two(str):
  return str[:2]

print(first_two("h"))



