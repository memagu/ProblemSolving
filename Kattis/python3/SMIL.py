# https://open.kattis.com/problems/smil

s = input()

smiles = [":)", ";)", ":-)", ";-)"]

for i, char in enumerate(s):
    for smile in smiles:
        count = 0
        for j in range(len(smile)):
            try:
                if s[i+j] == smile[j]:
                    count += 1
                if count == len(smile):
                    print(i)
            except Exception:
                continue