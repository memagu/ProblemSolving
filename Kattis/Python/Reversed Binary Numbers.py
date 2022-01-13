decimal_1 = input()
binary_1 = bin(int(decimal_1))[2:]
binary_2 = binary_1[len(binary_1)-1:0:-1]+binary_1[0]
decimal_2 = binary_2

print(int(decimal_2, 2))