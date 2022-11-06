from collections import defaultdict

cards = input().split()

counts = defaultdict(int)

for card in cards:
    counts[card[0]] += 1

print(sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][1])
