from itertools import combinations


def part1():
    with open("data.in", 'r') as f:
        lines = []
        for i, line in enumerate(f.read().splitlines()):
            lines.append(list(line))
            if line.count('.') == len(line):
                lines.append(list(line))

        added =0
        for col, column in enumerate(tuple(zip(*lines))):
            if column.count('.') == len(column):
                for line in lines:
                    line.insert(col+added, '.')
                added += 1

    galaxies = [(row, col) for row, line in enumerate(lines) for col, char in enumerate(line) if char == '#']

    return sum(abs(x2 - x1) + abs(y2 - y1) for (x1, y1), (x2, y2) in combinations(galaxies, 2))



def part2():
    with open("data.in", 'r') as f:
        lines = f.read().splitlines()

    horizontals = [i for i, line in enumerate(lines) if line.count('.') == len(line)]
    verticals = [i for i, col in enumerate(zip(*lines)) if col.count('.') == len(col)]
    galaxies = [(row, col) for row, line in enumerate(lines) for col, char in enumerate(line) if char == '#']

    result = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        distance = abs(x2 - x1) + abs(y2 - y1)
        for horizontal in horizontals:
            distance += 999_999 * (min(x1, x2) < horizontal < max(x1, x2))

        for vertical in verticals:
            distance += 999_999 * (min(y1, y2) < vertical < max(y1, y2))

        result += distance

    return result



if __name__ == "__main__":
    print(part1())
    print(part2())
