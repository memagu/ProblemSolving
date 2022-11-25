braille_to_num = {"*.....": '1',
                  "*.*...": '2',
                  "**....": '3',
                  "**.*..": '4',
                  "*..*..": '5',
                  "***...": '6',
                  "****..": '7',
                  "*.**..": '8',
                  ".**...": '9',
                  ".***..": '0'}

num_to_braille = {'1': "*.....",
                  '2': "*.*...",
                  '3': "**....",
                  '4': "**.*..",
                  '5': "*..*..",
                  '6': "***...",
                  '7': "****..",
                  '8': "*.**..",
                  '9': ".**...",
                  '0': ".***.."}

result = 0
for _ in range(2):
    digits = int(input())
    number = ["" for _ in range(digits)]

    for _ in range(3):
        for i, digit_part in enumerate(input().split()):
            number[i] += digit_part

    result += int("".join(map(lambda x: braille_to_num[x], number)))

for i in range(0, 6, 2):
    print(" ".join(num_to_braille[digit][i:i + 2] for digit in str(result)))
