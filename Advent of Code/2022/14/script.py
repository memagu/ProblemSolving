def part1():
    occupied = set()
    max_depth = 0

    with open("data.in", 'r') as f:
        for line in map(str.strip, f.readlines()):
            coordinates = tuple(map(lambda coord: tuple(map(int, coord.split(','))), line.split(" -> ")))

            for i in range(len(coordinates) - 1):
                start, end = coordinates[i:i + 2]
                max_depth = max(max_depth, start[1], end[1])

                if start[0] == end[0]:
                    for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                        occupied.add((start[0], y))
                    continue

                for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                    occupied.add((x, start[1]))

    rocks = len(occupied)
    abyss_reached = False

    while not abyss_reached:
        sand_pos = (500, 0)

        while True:
            if sand_pos[1] > max_depth:
                abyss_reached = True
                break

            for dx in (0, -1, 1):
                new_pos = (sand_pos[0] + dx, sand_pos[1] + 1)

                if new_pos not in occupied:
                    sand_pos = new_pos
                    break

            else:
                occupied.add(sand_pos)
                break

    return len(occupied) - rocks


def part2():
    occupied = set()
    max_depth = 0

    with open("data.in", 'r') as f:
        for line in map(str.strip, f.readlines()):
            coordinates = tuple(map(lambda coord: tuple(map(int, coord.split(','))), line.split(" -> ")))

            for i in range(len(coordinates) - 1):
                start, end = coordinates[i:i + 2]
                max_depth = max(max_depth, start[1], end[1])

                if start[0] == end[0]:
                    for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                        occupied.add((start[0], y))
                    continue

                for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                    occupied.add((x, start[1]))

    max_depth += 2
    rocks = len(occupied)
    source_reached = False

    while not source_reached:
        sand_pos = (500, 0)

        while True:
            for dx in (0, -1, 1):
                new_pos = (sand_pos[0] + dx, sand_pos[1] + 1)
                if new_pos not in occupied and new_pos[1] != max_depth:
                    sand_pos = new_pos
                    break

            else:
                if sand_pos == (500, 0):
                    source_reached = True

                occupied.add(sand_pos)
                break

    return len(occupied) - rocks


if __name__ == "__main__":
    print(part1())
    print(part2())
