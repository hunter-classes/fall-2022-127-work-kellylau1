# '''
# Directions: 
# input: a string in the form of "first last"
# returns: a string in the form of "F. Last"
# '''

# def initialize(): 
#   name = input("What is your full name? ")
#   split_name = name.split()
#   first = split_name[0]
#   first = first.upper()[:1]
#   last = split_name[1]
#   last = last.upper()[:1]
#   return first + "." + last

# print(initialize())







  

#------------------------------------------------------------

# '''
# Directions: 
# input: a string in the form of "first last"
# returns: a string in the form of "last first"
# '''

def bondify(name):  
  split_name = name.split()
  return split_name[1] + " " + split_name[0]

print(bondify("Kelly Lau"))





















# #------------------------------------------------------------
# '''
# Professor's Work:
# '''


# def initialize(name):
#     """
#     input: a string in the form "first last"
#     returns: a string in the form "F. Last"
#     """
#     result = ""
#     # isolate, uppercase and add first init to result
#     first = name[0]
#     first = first.upper()
#     result = result + first + "."

#     # find the last name (after space), cap it and add to result
#     location = name.find(' ')
#     last = name[location+1:].capitalize()
#     result = result + ' ' + last
#     return result
    
    
# def bondify(name):
#     """
#     input: a string in the form "first last"
#     returns: a string in the form "Last, First Last"
#     """
    
# # Test initialize
# result = initialize("james bond")
# print("james bond --> ",result)


# # Test Bondify



