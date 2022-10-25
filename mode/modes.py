# findSmallest(s) which takes in a list of numbers and returns the value of the smallest number

def findSmallest(s):
  s.sort()
  return s[0] 
s = [3,1,2]
print(findSmallest(s))


# freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the freuqeency of v, that is, the number of times that v appears in l.

def freq(l,v):

  for i in l: 
    if i < v or i > v:
      l.remove(i)
  return len(l)

l = [5,5,2,5,1,5]
freq(l,5)
  