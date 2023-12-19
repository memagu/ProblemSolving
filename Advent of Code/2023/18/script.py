def part1():
    direction_map = {
        'U': (0, -1),
        'D': (0, 1),
        'R': (1, 0),
        'L': (-1, 0),
    }

    with open("data.in", 'r') as f:
        instructions = [(direction_map[direction], int(steps)) for direction, steps, _ in
                        map(str.split, f.read().splitlines())]

    vertices = []
    prev_x = prev_y = min_x = min_y = max_x = max_y = 0
    for (dx, dy), steps in instructions:
        nx, ny = prev_x + dx * steps, prev_y + dy * steps
        prev_x, prev_y = nx, ny

        vertices.append((nx, ny))

        min_x = min(min_x, nx)
        min_y = min(min_y, ny)
        max_x = max(max_x, nx)
        max_y = max(max_y, ny)

    points_inside = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):

            hits = 0
            prev_vert_x, prev_vert_y = vertices[-1]
            for (vert_x, vert_y) in vertices:
                if x == vert_x and min(vert_y, prev_vert_y) <= y <= max(vert_y, prev_vert_y) or \
                        y == vert_y and min(vert_x, prev_vert_x) <= x <= max(vert_x, prev_vert_x):
                    break

                if vert_y != prev_vert_y:
                    hits += min(vert_y, prev_vert_y) <= y < max(vert_y, prev_vert_y) and vert_x < x

                prev_vert_x, prev_vert_y = vert_x, vert_y
            else:
                points_inside += hits % 2
                continue

            points_inside += 1

    return points_inside


def part2():
    direction_map = {
        '3': (0, -1),
        '1': (0, 1),
        '0': (1, 0),
        '2': (-1, 0),
    }

    with open("data.in", 'r') as f:
        instructions = [(direction_map[instruction[7]], int(instruction[2:7], 16)) for _, _, instruction in
                        map(str.split, f.read().splitlines())]

    x = y = area = 0
    for (dx, dy), steps in instructions:
        next_x, next_y = x + dx * steps, y + dy * steps
        area += x * next_y - y * next_x + max(abs(next_x - x), abs(next_y - y))
        x, y = next_x, next_y

    return 1 + abs(area) / 2


if __name__ == "__main__":
    print(part1())
    print(part2())
