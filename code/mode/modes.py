# # findLargest(l) which takes in a list of numbers and returns the value of the smallest number

# def findLargest(l):
#     l.sort()
#     return l[:1]

# l = [3, 1, 2]
# print(findLargest(l))

# # freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the freuqeency of v, that is, the number of times that v appears in l.

# def freq(l, v):

#     for i in l:
#         if i < v or i > v:
#             l.remove(i)
#     return len(l)

# l = [5, 5, 2, 5, 1, 5]
# print(freq(l, 5))

# Returns a mode of the dataset, that is the value that appears most frequently if multiple values appear the same # of times and are most frequent, return any of them.
# Ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the most mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4 since both of those values appear 3 times which is the most
# Strategy: assume the first value is the mode we can grab its frequency for each remaining item in the dataset:count that items frequence and see if it's the new mode so far

import datetime
import random


# def mode(dataset):
#     modeSoFar = dataset[0]
#     freqSoFar = freq(dataset, modeSoFar)
#     for item in dataset[1:]:
#         if freq(dataset, item) > freqSoFar:
#             modeSoFar = item
#             freqSoFar = freq(dataset, item)

#     return modeSoFar


# def testMode(size, maxValue):
#     dataset = buildRandomList(size, maxValue)
#     # print(dataset)
#     t = datetime.datetime.now()
#     starttime = t.microsecond / 1000
#     m = mode(dataset)
#     end = datetime.datetime.now()
#     elapsed = (end.microsecond / 1000) - starttime
#     print("size: ", size, " time: ", elapsed)

  

# def findLargest(dataset):
#     largeSoFar = dataset[0]
#     for item in dataset[1:]:
#         if item > largeSoFar:
#             largeSoFar = item
#     return largeSoFar



# def freq(dataset,v):
#     # since this loops over the entire data set once it takes n time 
#     #count = 0
#     #for item in dataset:
#     #    if item == v:
#     #        count = count + 1
#     #return count
#     return len([x for x in dataset if x == v])

# def buildRandomList(size,maxvalue):
#     #result = []
#     #for x in range(size):
#     #    result.append(random.randrange(maxvalue))
#     #return result
#     result = [random.randrange(maxvalue) for x in range(size)]
#     return result 


# def mode(dataset):
#     """
#     Returns a mode of the dataset, that is
#     the value that appears most frequently
#     if multiple values appear the same # of times and are
#     most frequent, return any of them.
#     Ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the most
#     mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4 since
#     both of those values appear 3 times which is the most
#     Strategy:
#     assume the first value is the mode
#     we can grab its frequency
#     for each remaining item in the dataset:
#       count that items frequence and see if it's the new
#       mode so far    
#     """
#     modeSoFar = dataset[0]
#     freqSoFar = dataset.count(modeSoFar)
#     for item in dataset[1:]: #outer loop -> n
#         # calling freq each time is n
#         # if freq(dataset,item) > freqSoFar:
#         if dataset.count(item) > freqSoFar:
#             modeSoFar = item
#             freqSoFar = dataset.count(item)
#     return modeSoFar



def fastMode(dataset):
  slots = []
  for i in range(100): 
    slots.append(0) 

    # this will store our tallies
  tallies = []
  for i in slots():
    tallies[i] += 1
    
    # 2. Loop through our dataset
    # and for each item incremement
    # (add 1) to the appropriate
    # slot in the tallies list
  find_mode = mode(tallies)
  print(find_mode)
    # 3. the index with the highest
    # value in tallies is the mode
fastMode(dataset)

  
    # pass

    
# def testMode(size,maxValue):
#     print("Dataset Size: ",size)
#     dataset = buildRandomList(size,maxValue)
#     # print(dataset)
#     m = mode(dataset)
#     print("Mode: ",m)

# def testFindLargest(size,maxValue):
#     print("Dataset Size: ",size)
#     dataset = buildRandomList(size,maxValue)
#     # print(dataset)
#     m = findLargest(dataset)
#     print("Largest: ",m)

# #testFindLargest(80000,30)
# testMode(40000,30)