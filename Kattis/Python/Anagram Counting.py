def factorial(n):
    result = n

    for i in range(n - 1, 1, -1):
        result *= i

    return result


while True:

    letters = {}

    try:
        s = input()
        n = len(s)

        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

        divider = 1

        for key in letters:
            divider *= factorial(letters[key])

        print(factorial(n) // divider)

    except EOFError:
        break
