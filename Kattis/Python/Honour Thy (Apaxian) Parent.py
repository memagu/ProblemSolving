y, p = input().split()
vowels_wo_e = ("a", "i", "o", "u")

if y.endswith("e"):
    print(y + "x" + p)

elif y.endswith(vowels_wo_e):
    print(y[:-1] + "ex" + p)

elif y.endswith("ex"):
    print(y + p)

else:
    print(y + "ex" + p)
    