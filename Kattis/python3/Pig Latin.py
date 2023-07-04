vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

while True:
    try:
        words = input().split()

        result = []
        for word in words:
            for i, letter in enumerate(word):
                if letter not in vowels:
                    continue

                if not i:
                    result.append(word + "yay")
                    break

                result.append(word[i:] + word[:i] + "ay")
                break

        print(" ".join(result))

    except EOFError:
        break
