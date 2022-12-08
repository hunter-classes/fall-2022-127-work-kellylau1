
import matplotlib.pyplot as plt

text_file = open("questions.txt", "r")

data = text_file.read().split()


for sentence in data:
    frequency = {}
    for word in data:
        frequency[word] = frequency.get(word, 0) + 1
print(frequency)

names = list(frequency.keys())
values = list(frequency.values())

plt.bar(range(len(frequency)), values, tick_label=names)
plt.show()
