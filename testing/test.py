x = 0b00000000000000000000000000001101
m = 0b00000000000000000000000000000001
a = 0b00000000000000000000000000000000
s =
for i in range(64):
    print(m & (x>>i), end="")