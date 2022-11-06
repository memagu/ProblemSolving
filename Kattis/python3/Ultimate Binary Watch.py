digits = list(map(int, input()))
for i, digit in enumerate(digits):
    binary = bin(digit).replace("0b", "")[::-1]
    while len(binary) < 4:
        binary += "0"
    digits[i] = binary

digits.insert(1, "    ")
digits.insert(3, "    ")
digits.insert(3, "    ")
digits.insert(3, "    ")
digits.insert(7, "    ")

for i in range(3, -1, -1):
    row = ""
    for j in range(9):
        row += digits[j][i].replace("0", ".").replace("1", "*")

    print(row)

