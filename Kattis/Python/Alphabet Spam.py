lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ws, lc, uc, sc = 0, 0, 0, 0

s = input()

for char in s:
    if char == "_":
        ws += 1
        continue

    if char in lowercase:
        lc += 1
        continue

    if char in uppercase:
        uc += 1
        continue

    sc += 1

print(ws / len(s))
print(lc / len(s))
print(uc / len(s))
print(sc / len(s))
