def part1():
    with open("data.in", 'r') as f:
        grid = tuple(map(list, f.read().splitlines()))

    for i in range(len(grid) - 1):
        for row in range(1, len(grid) - i):
            for col, char in enumerate(grid[row]):
                if char == 'O' and grid[row - 1][col] == '.':
                    grid[row][col] = '.'
                    grid[row - 1][col] = 'O'

    result = 0
    for row in range(len(grid)):
        for char in grid[row]:
            if char == 'O':
                result += len(grid) - row

    return result


def part2():
    with open("data.in", 'r') as f:
        grid = tuple(map(list, f.read().splitlines()))

    loads = []
    for _ in range(len(grid) + len(grid[0])):
        # north
        for i in range(len(grid) - 1):
            for row in range(1, len(grid) - i):
                for col in range(len(grid[0])):
                    if grid[row][col] == 'O' and grid[row - 1][col] == '.':
                        grid[row][col] = '.'
                        grid[row - 1][col] = 'O'

        # west
        for i in range(len(grid[0]) - 1):
            for col in range(1, len(grid[0]) - i):
                for row in range(len(grid)):
                    if grid[row][col] == 'O' and grid[row][col - 1] == '.':
                        grid[row][col] = '.'
                        grid[row][col - 1] = 'O'

        # south
        for i in range(len(grid) - 1):
            for row in range(len(grid) - 2, -1, -1):
                for col in range(len(grid[0])):
                    if grid[row][col] == 'O' and grid[row + 1][col] == '.':
                        grid[row][col] = '.'
                        grid[row + 1][col] = 'O'

        # east
        for i in range(len(grid[0]) - 1):
            for col in range(len(grid[0]) - 2, -1, -1):
                for row in range(len(grid)):
                    if grid[row][col] == 'O' and grid[row][col + 1] == '.':
                        grid[row][col] = '.'
                        grid[row][col + 1] = 'O'

        load = 0
        for row in range(len(grid)):
            for char in grid[row]:
                if char == 'O':
                    load += len(grid) - row

        loads.append(load)

    sequences = {}
    max_cycle = []
    start_index = 0
    for i in range(len(loads)):
        for j in range(i + len(max_cycle), len(loads)):
            cycle = tuple(loads[i:j + 1])
            if cycle in sequences and sequences[cycle] == i - len(cycle):
                if len(cycle) > len(max_cycle):
                    max_cycle = cycle
                    start_index = i - len(cycle)
            sequences[cycle] = i

    return max_cycle[(1_000_000_000 - start_index - 1) % len(max_cycle)]


if __name__ == "__main__":
    print(part1())
    print(part2())
