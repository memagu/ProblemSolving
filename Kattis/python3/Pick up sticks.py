from collections import defaultdict, deque

sticks, lines = map(int, input().split())

graph = defaultdict(list)
in_degree = defaultdict(int)

for _ in range(lines):
    upper_stick, lower_stick = map(int, input().split())
    graph[upper_stick].append(lower_stick)
    in_degree[lower_stick] += 1

queue = deque(node for node in range(1, sticks + 1) if not in_degree[node])

visited = set()
order = []

while queue:
    node = queue.popleft()
    if node in visited:
        print("IMPOSSIBLE")
        exit()

    order.append(node)
    visited.add(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

if len(order) != sticks:
    print("IMPOSSIBLE")
else:
    print(*order, sep='\n')
