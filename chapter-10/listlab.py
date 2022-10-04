# Write a function to find the smallest value in a list of items

#def smallest_value(list): 
  #list.sort()
  #return list[0]
  
#list = [1,5,3]
#print(smallest_value(list))


# Write a function that returns a new list that contains all the odd items in the original list

#def odd_items(list): 
  #result = []
  #for i in list: 
    #if i % 2 != 0:
      #result.append(i)
  #return result
  
#list = [2,3,4,5]
#print(odd_items(list))


# Write a function that takes a string and returns a new string where all the words are capitalized.

#def capitalize(string):
  #result = []
  #words = string.split()
  #for word in words: 
    #result.append(word.capitalize())
  #return ' '.join(result)

#string = "apple bob" 
#print(capitalize(string))


# Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case

#def upper(string):
  #result = []
  #words = string.split()
  #for word in words: 
    #if len(word) > 5:
      #result.append(word.upper())
    #else:
      #result.append(word)
  #return " ".join(result)

#string = "one two appler kellie"

#print(upper(string))


# Write a function that takes a list of numbers and returns a new list with each item squared

#def squared(num):
  #result = []
  #for number in num: 
    #result.append(number ** 2)
  #return result

#num = [1 , 2 , 3]

#print(squared(num))



# Write a function that takes two lists of numbers and returns a new list where each item is the corresponding values of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]

def add(list1, list2):
  result = []
  for idx, num in enumerate(list1): 
    result.append(num + list2[idx])

  return result 


list1 = [1 , 2 , 3]
list2 = [4 , 5 , 6]

print(add(list1, list2))















# chapter 10 # 10, 11, 12