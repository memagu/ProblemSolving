s = input()
result = []
tokens = {"L": -1, "R": 1}
pos = 0

for token in s:
    if token in ["L", "R"]:
        pos = max(pos + tokens[token], 0)
    elif token == "B":
        result.pop(pos - 1)
        pos = max(pos - 1, 0)
    else:
        result.insert(pos, token)
        pos += 1

print("".join(result))
