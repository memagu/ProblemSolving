# for token in s:
#     if token in ["L", "R"]:
#         pos = max(pos + tokens[token], 0)
#         pos += tokens[token]
#     elif token == "B":
#         result.pop(pos - 1)
#         pos = max(pos - 1, 0)
#         pos -= 1
#         result.pop(pos)
#     else:
#         result.insert(pos, token)
#         pos += 1

s = input()
result = []
tokens = {"L": -1, "R": 1, "B": -1}
pos = 0

for token in s:
    if token in ["L", "R", "B"]:
        pos += tokens[token]
        if token == "B":
            result.pop(pos)
    else:
        result.insert(pos, token)
        pos += 1

print("".join(result))
