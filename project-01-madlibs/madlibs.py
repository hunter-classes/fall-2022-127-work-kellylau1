22# Extras:
# - Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.
# - Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly. 

open_file = open("story.txt" , "r")
print(open_file.read())
open_file.close()

import random 

string = "Kelly <verb> around the <noun> yesterday because she felt sick. Then in the morning, she <verb> with the <noun> for five minutes."

string1 = "Rachel <verb> with the <adj> <noun> in the morning and then <verb> with the <adj> <noun> in the afternoon."

string2 = "<hero> <verb> with <pronoun> <noun> and then <hero> <verb> with <pronoun> <noun> later."

verbs = ['ate','walked','slept']
nouns = ['dog','hammer','cat','car','frog']
adjs = ['delicious', 'fast', 'jealous']
heros = ['Superman', 'WonderWoman', 'Batman']
pronouns = ['her', 'his']

words = string.split()
words1 = string1.split()
words2 = string2.split()

def substitute(words):
  
  for i in range(len(words)):
    if words[i] == '<verb>':
      words[i] = str(random.choice(verbs))

    if words[i] == '<noun>':
      words[i] = str(random.choice(nouns))    
        
  print(" ".join(words))
substitute(words)

def substitute1(words1):

  for i in range(len(words1)): 

    if words1[i] == '<verb>':
      words1[i] = str(random.choice(verbs))
       
    if words1[i] == '<adj>':
      words1[i] = str(random.choice(adjs))

    if words1[i] == '<noun>':
      words1[i] = str(random.choice(nouns))
  
  print(" ".join(words1))
substitute1(words1)


def substitute2(words2):

  for i in range(len(words2)): 
    if words2[i] == '<noun>':
      words2[i] = str(random.choice(nouns))
    
    if words2[i] == '<verb>':
      words2[i] = str(random.choice(verbs))
      
    if words2[i] == '<hero>':
      random.seed(1)
      choose_hero = str(random.choice(heros))
      words2[i] = choose_hero
      
    if words2[i] == '<pronoun>':
      random.seed(1)
      choose_pronoun = str(random.choice(pronouns))
      words2[i] = choose_pronoun    
      
  print(" ".join(words2))
substitute2(words2)

 
