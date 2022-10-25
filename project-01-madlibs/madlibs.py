import random 

string = "Sam <verb> the <noun> and then <verb> the <noun> later."

verbs = ['ate','walked','slept']
nouns = ['dog','hammer','cat','car','frog']

words = string.split()

def substitute(words):
  for verb in words: 
    verb == "<verb>"
    random_verb = random.choice(verbs)
    verb = verb.replace(verb, random_verb)
  print(str(verb))
  for noun in words: 
    noun == "<noun>"
    random_noun = random.choice(nouns)
    noun = noun.replace(noun, random_noun)
  print(str(noun))

print(words)


  



      
    


