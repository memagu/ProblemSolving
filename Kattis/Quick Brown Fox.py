
def string_to_characters(string):
    return [character for character in string]


n = int(input())
alphabet = []

for letter in (range(97, 97 + 26)):
    alphabet.append(chr(letter))

for x in range(n):

    listed_string = string_to_characters(input())
    missing_letters = []

    for index in range(len(listed_string)):
        listed_string[index] = listed_string[index].lower()

    for letter in alphabet:
        if letter not in listed_string:
            missing_letters.append(letter)

    if len(missing_letters) == 0:
        print("pangram")
    else:
        missing_letters.insert(0, "missing ")
        print(*missing_letters, sep="")
