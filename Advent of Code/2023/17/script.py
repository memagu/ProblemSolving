import heapq


def part1():
    direction_map = {
        (0, -1): ((1, 0), (-1, 0)),
        (0, 1): ((1, 0), (-1, 0)),
        (1, 0): ((0, -1), (0, 1)),
        (-1, 0): ((0, -1), (0, 1))
    }

    with open("data.in", 'r') as f:
        grid = tuple(tuple(map(int, line)) for line in f.read().splitlines())

    heap = [
        (grid[1][0], (0, 1), (0, 1)),
        (grid[1][0] + grid[2][0], (0, 2), (0, 1)),
        (grid[1][0] + grid[2][0] + grid[3][0], (0, 3), (0, 1)),
        (grid[0][1], (1, 0), (1, 0)),
        (grid[0][1] + grid[0][2], (2, 0), (1, 0)),
        (grid[0][1] + grid[0][2] + grid[0][3], (3, 0), (1, 0))
    ]

    heapq.heapify(heap)

    min_heat_loss = {
        ((0, 0), (0, -1)): grid[0][0],
        ((0, 0), (0, 1)): grid[0][0],
        ((0, 0), (1, 0)): grid[0][0],
        ((0, 0), (-1, 0)): grid[0][0]
    }

    while heap:
        heat_loss, (x, y), direction = heapq.heappop(heap)

        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            return heat_loss

        for dx, dy in direction_map[direction]:
            for steps in range(1, 4):
                nx, ny = x + dx * steps, y + dy * steps
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    new_heat_loss = heat_loss + sum(grid[y + dy * substep][x + dx * substep] for substep in range(1, steps + 1))
                    if ((nx, ny), (dx, dy)) not in min_heat_loss or new_heat_loss < min_heat_loss[((nx, ny), (dx, dy))]:
                        heapq.heappush(heap, (new_heat_loss, (nx, ny), (dx, dy)))
                        min_heat_loss[((nx, ny), (dx, dy))] = new_heat_loss


def part2():
    direction_map = {
        (0, -1): ((1, 0), (-1, 0)),
        (0, 1): ((1, 0), (-1, 0)),
        (1, 0): ((0, -1), (0, 1)),
        (-1, 0): ((0, -1), (0, 1))
    }

    with open("data.in", 'r') as f:
        grid = tuple(tuple(map(int, line)) for line in f.read().splitlines())

    heap = [
        (0, (0, 0), (0, 1)),
        (0, (0, 1), (1, 0)),
    ]

    heapq.heapify(heap)

    min_heat_loss = {
        ((0, 0), (0, -1)): grid[0][0],
        ((0, 0), (0, 1)): grid[0][0],
        ((0, 0), (1, 0)): grid[0][0],
        ((0, 0), (-1, 0)): grid[0][0]
    }

    while heap:
        heat_loss, (x, y), direction = heapq.heappop(heap)

        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            return heat_loss

        for dx, dy in direction_map[direction]:
            for steps in range(4, 11):
                nx, ny = x + dx * steps, y + dy * steps
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    new_heat_loss = heat_loss + sum(grid[y + dy * substep][x + dx * substep] for substep in range(1, steps + 1))
                    if ((nx, ny), (dx, dy)) not in min_heat_loss or new_heat_loss < min_heat_loss[((nx, ny), (dx, dy))]:
                        heapq.heappush(heap, (new_heat_loss, (nx, ny), (dx, dy)))
                        min_heat_loss[((nx, ny), (dx, dy))] = new_heat_loss


if __name__ == "__main__":
    print(part1())
    print(part2())
