from collections import defaultdict
from heapq import heappop, heappush
from sys import setrecursionlimit
from typing import Dict, List, Tuple

setrecursionlimit(10 << 16)


def get_graph_node_info(node: str, parent: str, graph: Dict[str, List[str]]) -> Dict[str, Tuple[int, str, str]]:  # {node: (max_depth, deepest_leaf, parent)}
    children = graph[node]

    if not children:
        return {node: (0, node, parent)}

    info_map = {}
    child_with_max_depth = (0, "")
    for child in children:
        info_map.update(get_graph_node_info(child, node, graph))
        child_info = info_map[child]

        if child_info[0] <= child_with_max_depth[0]:
            child_with_max_depth = (child_info[0], child_info[1])

    info_map[node] = (child_with_max_depth[0] - 1, child_with_max_depth[1], parent)

    return info_map


n = int(input())  # Antalet städer

graph = defaultdict(list)
for _ in range(n - 1):
    parent, child = input().split()

    graph[parent].append(child)

    if child not in graph:
        graph[child] = []

graph_info = get_graph_node_info('0', '-1', graph)

visited = {'-1'}
queue = [(graph_info['0'], '0')]
front_cities = 1

result = []

while queue:
    node = heappop(queue)[0][1]

    while node not in visited:
        result.append(front_cities)

        for child in (child for child in graph[node] if child not in visited):
            heappush(queue, (graph_info[child], child))

        visited.add(node)
        node = graph_info[node][2]

    front_cities += 1

print(" ".join(map(str, result[1:])))
