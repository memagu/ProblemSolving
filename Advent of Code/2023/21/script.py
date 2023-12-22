from collections import deque

import numpy as np


def part1():
    with open("data.in", 'r') as f:
        grid = f.read().splitlines()

    start = next((x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'S')

    queue = deque((start,))
    for _ in range(64):
        reachable = set()
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != '#':
                    reachable.add((nx, ny))

        queue.extend(reachable)

    return len(queue)


def part2():
    with open("data.in", 'r') as f:
        grid = f.read().splitlines()

    width, height = len(grid[0]), len(grid)
    start = next((x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'S')

    assert width == height and start[0] == width // 2

    n_reached = []
    for steps in (width // 2 + width * i for i in range(3)):
        queue = deque((start,))
        visited = {}

        for step in range(steps):
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                    nx, ny = x + dx, y + dy
                    if grid[ny % width][nx % height] != '#' and (nx, ny) not in visited:
                        visited[(nx, ny)] = step
                        queue.append((nx, ny))

        n_reached.append(sum(i % 2 != steps % 2 for _, i in visited.items()))

    poly = np.polyfit(*zip(*enumerate(n_reached)), 2)
    grids = 26501365 // width

    return round(np.polyval(poly, grids))


if __name__ == "__main__":
    print(part1())
    print(part2())
