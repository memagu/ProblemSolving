"""
# Slow O(n^2) | (n/2)^2

necklace = input()
split_length = len(necklace) >> 1

result = 0

for i in range(split_length):
    left_blues = right_blues = 0

    for j in range(split_length):
        if necklace[i-j] == "B":
            left_blues += 1

        if necklace[(i + j + 1) % len(necklace)] == "B":
            right_blues += 1

    result = max(result, left_blues, right_blues)

print(result)
"""

# O(n) | 1.5n

necklace = input()
half_necklace_len = len(necklace) >> 1
current = result = sum(necklace[i] == 'B' for i in range(half_necklace_len))

for i in range(len(necklace)):
    current += (necklace[(i + half_necklace_len) % len(necklace)] == 'B') - (necklace[i] == 'B')
    result = max(result, current)

print(result)
