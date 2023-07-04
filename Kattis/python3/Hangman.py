unique_letters = set(input())

right = wrong = 0
for letter in input():
    if letter in unique_letters:
        right += 1
        if right == len(unique_letters):
            print("WIN")
            break
        continue

    wrong += 1
    if wrong == 10:
        print("LOSE")
        break
