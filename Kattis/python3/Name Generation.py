import random

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

generated_names = set()

n = int(input())

while len(generated_names) < n:
    name = ""
    for i in range(random.randint(3, 20)):
        if i % 3 == 0:
            name += random.choice(vowels)
        else:
            name += random.choice(consonants)

    generated_names.add(name)

for name in generated_names:
    print(name)



