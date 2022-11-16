from collections import deque


consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}

result = ""
last = deque(maxlen=2)

for char in input():
    if char not in consonants or last.count(char) != 2:
        result += char

    last.append(char)

print(result)
