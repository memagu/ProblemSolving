vowels = ["a", "e", "i", "o", "u", "y"]

while True:
    try:
        words = input().split()

        result = ""
        for word in words:
            if word[0] in vowels:
                result += " " + word + "yay"
                continue
            for i, char in enumerate(word):
                if char in vowels:
                    result += " " + word[i:] + word[:i] + "ay"
                    break

        print(result.strip())

    except EOFError:
        break
        