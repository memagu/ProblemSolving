from collections import defaultdict


def part1():
    direction_map = {
        '.': ((0, -1), (0, 1), (1, 0), (-1, 0)),
        '^': ((0, -1),),
        'v': ((0, 1),),
        '>': ((1, 0),),
        '<': ((-1, 0),),
    }

    with open("data.in", 'r') as f:
        grid = f.read().splitlines()

    start_x, start_y = next((x, 0) for x, char in enumerate(grid[0]) if char == '.')
    end_x, end_y = next((x, len(grid) - 1) for x, char in enumerate(grid[-1]) if char == '.')

    queue = [(start_x, start_y, set())]
    max_distance = 0
    while queue:
        x, y, path = queue.pop()
        if (x, y) == (end_x, end_y):
            max_distance = max(max_distance, len(path))
            continue

        char = grid[y][x]

        if char == '#':
            continue

        for dx, dy in direction_map[char]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and (nx, ny) not in path:
                queue.append((nx, ny, path.union({(nx, ny), })))

    return max_distance


def part2():
    with open("data.in", 'r') as f:
        grid = f.read().splitlines()

    start = next((x, 0) for x, char in enumerate(grid[0]) if char == '.')
    end = next((x, len(grid) - 1) for x, char in enumerate(grid[-1]) if char == '.')

    graph = defaultdict(dict)

    queue = [start]
    while queue:
        (x, y) = queue.pop()

        connected_tiles = [(nx, ny) for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)) if
                           0 <= (nx := x + dx) < len(grid[0]) and 0 <= (ny := y + dy) < len(grid) and grid[ny][
                               nx] != '#']

        for tile in connected_tiles:
            if (x, y) in graph and tile in graph[(x, y)]:
                continue

            graph[(x, y)][tile] = 1
            graph[tile][(x, y)] = 1

            queue.append(tile)

    for node, edges in tuple(graph.items()):
        if len(edges) != 2:
            continue

        (neighbour_1, distance_1), (neighbour_2, distance_2) = edges.items()

        new_distance = distance_1 + distance_2

        if neighbour_2 in graph[neighbour_1]:
            new_distance = max(new_distance, graph[neighbour_1][neighbour_2])

        graph[neighbour_1][neighbour_2] = new_distance
        graph[neighbour_2][neighbour_1] = new_distance

        del graph[neighbour_1][node]
        del graph[neighbour_2][node]

        del graph[node]

    queue = [(start, {start, }, 0)]
    max_distance = 0
    while queue:
        node, path, path_length = queue.pop()
        if node == end:
            max_distance = max(max_distance, path_length)
            continue

        for child, edge_length in graph[node].items():
            if child in path:
                continue

            queue.append((child, path.union({child, }), path_length + edge_length))

    return max_distance


if __name__ == "__main__":
    print(part1())
    print(part2())
