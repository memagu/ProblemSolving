table = {"A": [11, 11],
         "K": [4, 4],
         "Q": [3, 3],
         "J": [20, 2],
         "T": [10, 10],
         "9": [14, 0],
         "8": [0, 0],
         "7": [0, 0]}

hands, dominant = input().split()
hands = int(hands)

score = 0
for _ in range(4 * hands):
    value, suit = input()
    if suit == dominant:
        score += table[value][0]
        continue

    score += table[value][1]

print(score)