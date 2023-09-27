"""
from collections import deque


def diff_count(a: str, b: str) -> int:
    count = 0
    for char_a, char_b in zip(a, b):
        count += char_a != char_b
    return count


n, m, k = map(int, input().split())
genomes = [input() for _ in range(n)]

queue = deque([(0, genomes[0])])  # (index, genome)
skip = set()

while queue:
    i, genome = queue.popleft()
    if genome in skip:
        continue

    found = True

    for j, other_genome in enumerate(genomes):
        if i == j:
            continue

        if diff_count(genome, other_genome) != k:
            found = False
            skip.add(genome)
            continue

        queue.append((j, other_genome))

    if found:
        print(i + 1)
        break
"""

n, m, k = map(int, input().split())
genomes = [input() for _ in range(n)]



