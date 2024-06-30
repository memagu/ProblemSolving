words = sorted((input() for _ in range(int(input()))), key=lambda word: len(set(word)))

while True:
    current_word = words.pop()
    print(current_word, flush=True)
    clue = input()
    if clue == "OOOOO":
        break
    for i, (char, char_clue) in enumerate(zip(current_word, clue)):
        match char_clue:
            case 'X':
                char_occurences = 0
                for j, char_check in enumerate(current_word):
                    if char_check == char and clue[j] in "/O":
                        char_occurences += 1

                potential_words = set()
                for word in words:
                    if word.count(char) == char_occurences:
                        potential_words.add(word)
                words = potential_words
            case '/':
                potential_words = set()
                for word in words:
                    if word[i] != char and char in word:
                        potential_words.add(word)
                words = potential_words
            case 'O':
                potential_words = set()
                for word in words:
                    if word[i] == char:
                        potential_words.add(word)
                words = potential_words
