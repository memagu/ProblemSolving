from collections import deque
from typing import List, Tuple


def shortest_path_faster_algorithm(graph: List[List[Tuple[int, float]]], source: int) -> List[float]:
    connected_edges = deque()
    queue = [source]
    visited = {source}

    while queue:
        vertex = queue.pop()
        for child, weight in graph[vertex]:
            connected_edges.append((vertex, child, weight))
            if child not in visited:
                queue.append(child)
                visited.add(child)

    edge_queue = connected_edges.copy()
    vertex_dist = [float("inf") for _ in graph]
    vertex_dist[source] = 0
    vertex_len = [0 for _ in graph]

    loop_detector = set()

    while edge_queue:
        if not edge_queue:
            break

        t_edge_queue = tuple(edge_queue)
        if t_edge_queue in loop_detector:
            for edge_source, edge_destination, edge_weight in edge_queue:
                vertex_dist[edge_destination] = float("-inf")
            break

        loop_detector.add(t_edge_queue)

        added = set()

        for _ in range(len(edge_queue)):
            edge_source, edge_destination, edge_weight = edge_queue.popleft()
            vertex_len[edge_source] += 1
            if vertex_dist[edge_source] + edge_weight < vertex_dist[edge_destination]:
                if vertex_len[edge_source] == len(graph):
                    vertex_dist[edge_destination] = float("-inf")
                else:
                    vertex_dist[edge_destination] = vertex_dist[edge_source] + edge_weight

                if edge_source in added:
                    continue

                add_queue = [edge_destination]
                while add_queue:
                    vertex = add_queue.pop()
                    for child, weight in graph[vertex]:
                        if child in added:
                            continue

                        added.add(child)
                        add_queue.append(child)
                        edge_queue.append((vertex, child, weight))

    return vertex_dist


while True:
    n, m, q, s = map(int, input().split())

    if n == m == q == s == 0:
        break

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    vertex_distances_from_s = shortest_path_faster_algorithm(graph, 0)

    for _ in range(q):
        result = vertex_distances_from_s[int(input())]

        if result == float("inf"):
            print("Impossible")
            continue

        if result == float("-inf"):
            print("-Infinity")
            continue

        print(result)
