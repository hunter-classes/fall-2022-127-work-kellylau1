'''
Directions - 
input: a string in the form of "first last"
returns: a string in the form of "last first"
'''

# def bondify(name):
#   split_name = name.split()
#   return split_name[1] + " " + split_name[0]

# print(bondify("Kelly Lau"))

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

# def piglatin_simple(word):
# if word[0] == ["a", "e", "i", "o", "u"]:
#     return word[1:] + word[0] + "ay"
# else:
#     return word + "yay"

# print(piglatin_simple("hello"))

#------------------------------------------------------------------------
# '''
# TODO:
# 1. Make it work for capitalized words
#    ex: Cable -> Ablecay
# 2. Handle periods (and possibly other punctuation)
#    ex: Able. -> Ableay.
#        cable. -> ablecay.
#        '''

# def piglatinn(word):
#     simple_word = word.lower()
#     has_period = word[-1] == '.'
#     capitalize = word[0].isupper()
#     if has_period:
#       simple_word = simple_word[:-1]
#     result = ''

#     if simple_word[0] == ["a", "e", "i", "o", "u"]:
#       result = simple_word[1:] + simple_word[0] + "ay"
#     else:
#       result = simple_word + "yay"

#     if has_period:
#       result = result + '.'
#     if capitalize:
#         return result[0].upper() + result[1:]
#     return result


def piglatin(word):
    if word[-1] == '.':
        if word[0].isupper():
            if word[0] not in 'AEIOU':
                return word[1].upper() + word[2:-1] + word[0].lower(
                ) + "ay" + "."
            else:
                return word[:-1] + "yay" + "."
        else:
            if word[0] not in 'aeiou':
                return word[1:-1] + word[0] + "yay" +'.'
            else:
                return word[:-1] + "ay" + '.'
    else:
        if word[0].isupper():
            if word[0] not in 'AEIOU':
                return word[1].upper() + word[2:] + word[0].lower() + "ay"
            else:
                return word + "yay"
        else:
            if word[0] in 'aeiou':
                return word[1:] + word[0] + "ay"
            else:
                return word + "yay"


print(piglatin("Able"))


