from collections import deque


def part1():
    pipes = {
        '|': ((0, -1), (0, 1)),
        '-': ((1, 0), (-1, 0)),
        'L': ((0, -1), (1, 0)),
        'J': ((0, -1), (-1, 0)),
        '7': ((0, 1), (-1, 0)),
        'F': ((0, 1), (1, 0))
    }

    with open("data.in", 'r') as f:
        grid = [line for line in f.read().splitlines()]

    queue = None
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == 'S':
                queue = deque(
                    (nx, ny)
                    for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)) if grid[(ny := y + dy)][(nx := x + dx)] in pipes
                    for px, py in pipes[grid[ny][nx]] if dx + px == 0 and dy + py == 0
                )
                break

    depth = 0
    visited = set(queue)
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if not grid[y][x] in pipes:
                continue

            for dx, dy in pipes[grid[y][x]]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        depth += 1

    return depth


def part2():
    pipes = {
        '|': ((0, -1), (0, 1)),
        '-': ((1, 0), (-1, 0)),
        'L': ((0, -1), (1, 0)),
        'J': ((0, -1), (-1, 0)),
        '7': ((0, 1), (-1, 0)),
        'F': ((0, 1), (1, 0))
    }

    with open("data.in", 'r') as f:
        grid = [line for line in f.read().splitlines()]

    start = None
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == 'S':
                start = (x, y)
                break

    point = next(
        (nx, ny)
        for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)) if grid[(ny := start[1] + dy)][(nx := start[0] + dx)] in pipes
        for px, py in pipes[grid[ny][nx]] if dx + px == 0 and dy + py == 0
    )

    min_x, min_y = len(grid[0]) - 1, len(grid) - 1
    max_x = max_y = 0
    queue = [point]
    visited = {point}
    vertices = [start]
    while queue:
        x, y = queue.pop()

        if not grid[y][x] in pipes:
            continue

        for dx, dy in pipes[grid[y][x]]:
            nx, ny = x + dx, y + dy

            if vertices[-1][0] != nx and vertices[-1][1] != ny:
                vertices.append((x, y))

            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    points_inside = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in visited:
                continue

            hits = 0
            last_vertex = vertices[-1]
            for vertex in vertices:
                if vertex[1] == last_vertex[1]:
                    last_vertex = vertex
                    continue

                hits += min(vertex[1], last_vertex[1]) <= y < max(vertex[1], last_vertex[1]) and vertex[0] < x

                last_vertex = vertex

            points_inside += hits % 2

    return points_inside


if __name__ == "__main__":
    print(part1())
    print(part2())
