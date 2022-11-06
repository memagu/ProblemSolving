letters = input()
must_contain = letters[0]

for _ in range(int(input())):
    word = input()
    if must_contain not in word or len(word) < 4:
        continue

    for char in set(word):
        if char not in letters:
            break
    else:
        print(word)
