from functools import reduce


def part1():
    with open("data.in", 'r') as f:
        readings = [tuple(map(int, line.split())) for line in f.read().splitlines()]

    result = 0
    for values in readings:
        differences = [values]
        while any(differences[-1]):
            differences.append([differences[-1][i + 1] - differences[-1][i] for i in range(len(differences[-1]) - 1)])

        result += sum(diffs[-1] for diffs in differences)

    return result


def part2():
    with open("data.in", 'r') as f:
        readings = [tuple(map(int, line.split())) for line in f.read().splitlines()]

    result = 0
    for values in readings:
        differences = [values]
        while any(differences[-1]):
            differences.append([differences[-1][i + 1] - differences[-1][i] for i in range(len(differences[-1]) - 1)])

        result += reduce(lambda extrapolation, diffs: diffs[0] - extrapolation, reversed(differences), 0)

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
