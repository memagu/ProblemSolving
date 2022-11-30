from collections import defaultdict
from sys import setrecursionlimit
from typing import Dict, List, Optional, Set

"""
def paths_to_node(node: str, graph: Dict[str, List[str]], paths: Optional[Dict[str, List[str]]] = None) -> Dict[str, List[str]]:
    if paths is None:
        paths = {node: [node]}

    for child in graph[node]:
        paths[child] = [child, *paths[node]]
        paths_to_node(child, graph, paths)

    return paths
"""


def max_depths_from_node(node: str, graph: Dict[str, List[str]]) -> Dict[str, int]:
    children = graph[node]

    if not children:
        return {node: 0}

    max_depths = {}
    for child in children:
        max_depths.update(max_depths_from_node(child, graph))  # O(1)

    max_depths[node] = max(max_depths[child] for child in children) + 1

    return max_depths


setrecursionlimit(10 << 16)

n = int(input())  # Antalet städer

graph = defaultdict(list)
for _ in range(n - 1):
    parent, child = input().split()

    graph[parent].append(child)

    if child not in graph:
        graph[child] = []

print(max_depths_from_node('0', graph))
