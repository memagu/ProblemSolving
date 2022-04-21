s = input()
for i, char in enumerate(s):
    if char == '(':
        if len(s) / 2 - 1 == i:
            print("correct")
        else:
            print("fix")
        break
