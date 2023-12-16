def part1():
    direction_map = {
        '.': {
            (0, -1): ((0, -1), None),
            (0, 1): ((0, 1), None),
            (1, 0): ((1, 0), None),
            (-1, 0): ((-1, 0), None),
        },
        '/': {
            (0, -1): ((1, 0), None),
            (0, 1): ((-1, 0), None),
            (1, 0): ((0, -1), None),
            (-1, 0): ((0, 1), None),
        },
        '\\': {
            (0, -1): ((-1, 0), None),
            (0, 1): ((1, 0), None),
            (1, 0): ((0, 1), None),
            (-1, 0): ((0, -1), None),
        },
        '|': {
            (0, -1): ((0, -1), None),
            (0, 1): ((0, 1), None),
            (1, 0): ((0, -1), (0, 1)),
            (-1, 0): ((0, -1), (0, 1)),
        },
        '-': {
            (0, -1): ((1, 0), (-1, 0)),
            (0, 1): ((1, 0), (-1, 0)),
            (1, 0): ((1, 0), None),
            (-1, 0): ((-1, 0), None),
        }
    }  # direction_map = {symbol: {source_direction: (target_direction_1, target_direction_2)}}

    with open("data.in", 'r') as f:
        grid = f.read().splitlines()

    energized = {(0, 0), }  # {(position_x, position_y),}
    queue = [((0, 0), (1, 0))]  # queue = [((position_x, position_y)), (direction_x, direction_y)))]
    visited = set(queue)
    while queue:
        (position_x, position_y), direction = queue.pop()

        for new_direction in direction_map[grid[position_y][position_x]][direction]:
            if new_direction is None:
                continue

            dx, dy = new_direction
            nx, ny = position_x + dx, position_y + dy
            new = ((nx, ny), new_direction)

            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and new not in visited:
                visited.add(new)
                queue.append(new)
                energized.add((nx, ny))

    return len(energized)


def part2():
    direction_map = {
        '.': {
            (0, -1): ((0, -1), None),
            (0, 1): ((0, 1), None),
            (1, 0): ((1, 0), None),
            (-1, 0): ((-1, 0), None),
        },
        '/': {
            (0, -1): ((1, 0), None),
            (0, 1): ((-1, 0), None),
            (1, 0): ((0, -1), None),
            (-1, 0): ((0, 1), None),
        },
        '\\': {
            (0, -1): ((-1, 0), None),
            (0, 1): ((1, 0), None),
            (1, 0): ((0, 1), None),
            (-1, 0): ((0, -1), None),
        },
        '|': {
            (0, -1): ((0, -1), None),
            (0, 1): ((0, 1), None),
            (1, 0): ((0, -1), (0, 1)),
            (-1, 0): ((0, -1), (0, 1)),
        },
        '-': {
            (0, -1): ((1, 0), (-1, 0)),
            (0, 1): ((1, 0), (-1, 0)),
            (1, 0): ((1, 0), None),
            (-1, 0): ((-1, 0), None),
        }
    }  # direction_map = {symbol: {source_direction: (target_direction_1, target_direction_2)}}

    with open("data.in", 'r') as f:
        grid = f.read().splitlines()

    width, height = len(grid[0]), len(grid)
    starts = [((x, 0), (0, 1)) for x in range(width)] + \
             [((x, height - 1), (0, -1)) for x in range(width)] + \
             [((0, y), (1, 0)) for y in range(height)] + \
             [((width - 1, y), (-1, 0)) for y in range(height)]

    max_energized = 0
    for (start_x, start_y), (start_dir_x, start_dir_y) in starts:
        energized = {(start_x, start_y), }
        queue = [((start_x, start_y), (start_dir_x, start_dir_y))]
        visited = set(queue)
        while queue:
            (position_x, position_y), direction = queue.pop()

            for new_direction in direction_map[grid[position_y][position_x]][direction]:
                if new_direction is None:
                    continue

                dx, dy = new_direction
                nx, ny = position_x + dx, position_y + dy
                new = ((nx, ny), new_direction)

                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and new not in visited:
                    visited.add(new)
                    queue.append(new)
                    energized.add((nx, ny))

        max_energized = max(len(energized), max_energized)

    return max_energized


if __name__ == "__main__":
    print(part1())
    print(part2())
