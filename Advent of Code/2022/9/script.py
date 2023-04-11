def part1():
    x_head = y_head = x_tail = y_tail = 0
    visited = set()

    with open("data.in", 'r') as f:
        for line in f.readlines():
            direction, steps = line.strip().split()
            steps = int(steps)

            for _ in range(steps):
                match direction:
                    case 'R':
                        x_head += 1
                    case 'L':
                        x_head -= 1
                    case 'U':
                        y_head += 1
                    case 'D':
                        y_head -= 1

                if (x_head - x_tail) ** 2 + (y_head - y_tail) ** 2 > 2:
                    match direction:
                        case 'R':
                            x_tail, y_tail = x_head - 1, y_head
                        case 'L':
                            x_tail, y_tail = x_head + 1, y_head
                        case 'U':
                            x_tail, y_tail = x_head, y_head - 1
                        case 'D':
                            x_tail, y_tail = x_head, y_head + 1

                visited.add((x_tail, y_tail))

    return len(visited)


def part2():
    knots = [(0, 0) for _ in range(10)]
    visited = set()

    with open("data.in", 'r') as f:
        for line in f.readlines():
            direction, steps = line.strip().split()
            steps = int(steps)

            for _ in range(steps):
                match direction:
                    case 'R':
                        knots[0] = knots[0][0] + 1, knots[0][1]
                    case 'L':
                        knots[0] = knots[0][0] - 1, knots[0][1]
                    case 'U':
                        knots[0] = knots[0][0], knots[0][1] + 1
                    case 'D':
                        knots[0] = knots[0][0], knots[0][1] - 1

                for i in range(len(knots) - 1):
                    if (knots[i][0] - knots[i + 1][0]) ** 2 + (knots[i][1] - knots[i + 1][1]) ** 2 <= 2:
                        continue

                    closest_pos = float("inf"), (0, 0)
                    for x in range(-1, 2):
                        scan_x = x + knots[i + 1][0]

                        for y in range(-1, 2):
                            if not (x or y):
                                continue

                            scan_y = y + knots[i + 1][1]

                            if (knots[i][0] - scan_x) ** 2 + (knots[i][1] - scan_y) ** 2 >= closest_pos[0]:
                                continue

                            closest_pos = (knots[i][0] - scan_x) ** 2 + (knots[i][1] - scan_y) ** 2, (scan_x, scan_y)

                    knots[i + 1] = closest_pos[1]

                visited.add(tuple(knots[-1]))

    return len(visited)


if __name__ == "__main__":
    print(part1())
    print(part2())
