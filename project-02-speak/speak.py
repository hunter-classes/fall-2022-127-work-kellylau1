

with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')

dictionary = {'Hello': 'Ahoy', 'friend': 'mate', 'wife': 'lady', 'cooking': 'cookin', 'food': 'chow'}

list = data.split()

def substitute(word):
  result = []
  
  for word in list: 
    has_comma = word[-1] == ','
    has_exclamation = word[-1] == '!'
      
    if has_comma or has_exclamation:
      word = word[:-1]

    new_word = word    
    if word in dictionary:
      new_word = dictionary[word]

    if has_comma: 
      new_word += ','
    if has_exclamation: 
      new_word = new_word + '!'    
     
    result.append(new_word)   
  return " ".join(result)

print(substitute(list))


