'''
Directions - 
input: a string in the form of "first last"
returns: a string in the form of "last first"
'''

def bondify(name):  
  split_name = name.split()
  return split_name[1] + " " + split_name[0]

print(bondify("Kelly Lau"))


#------------------------------------------------------------
'''
Directions - 
input: a string representing a word
returns: a new string with the word converted to piglatin

Rules:
if the first letter is a consonent, move it from the start to the end and add "ay"
so "hello" becomes "ellohay"

If the first letter is a vowel, just add "yay" to the end

try to also handle upper case words
'''


'''
Make sure to test from the bottom of your program - when run, it should call piglatin
on various words and print out the word and the results
'''


def piglatinn(word):
  if word[0] == ["a", "e", "i", "o", "u"]:
    return word[1:] + word[0] + "ay"
  else: 
    return word + "yay"
print(piglatinn("hello"))