from collections import defaultdict, deque

n = int(input())

graph = defaultdict(list)
for _ in range(n - 1):
    parent, child = input().split()

    graph[parent].append(child)

    if child not in graph:
        graph[child] = []

widths = []
visited = set()
queue = deque(graph['0'])

while queue:
    widths.append(len(queue))
    for _ in range(len(queue)):
        current_node = queue.popleft()

        for child in graph[current_node]:
            if child in visited:
                continue

            visited.add(child)
            queue.append(child)

result = []
depth_sum = sum(widths)
i = 0

while depth_sum:
    forks = i // len(widths) + 1
    j = i % len(widths)
    if widths[j]:
        widths[j] -= 1
        depth_sum -= 1
        result.append(str(forks))
    i += 1

print(" ".join(result))
