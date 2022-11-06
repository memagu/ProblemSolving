def clamp(val, min_val, max_val):
    return max(min(val, max_val), min_val)


instructions = int(input())
volume = 7

for _ in range(instructions):
    if input() == "Skru op!":
        volume = clamp(volume + 1, 0, 10)
    else:
        volume = clamp(volume - 1, 0, 10)

print(volume)

