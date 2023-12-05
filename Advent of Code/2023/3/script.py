import math
import re


def part1():
    with open("data.in", 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    result = 0
    for i, number in ((i, number) for i, row in enumerate(grid) for number in re.finditer(r"\d+", row)):
        for x in range(max(0, number.start() - 1), min(len(grid[0]), number.end() + 1)):
            for y in range(max(0, i - 1), min(len(grid), i + 2)):
                char = grid[y][x]
                if char.isdigit() or char == '.':
                    continue
                result += int(number.group())
                break
            else:
                continue
            break

    return result


def part2():
    with open("data.in", 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    numbers = [(y, number.start(), number.end(), int(number.group())) for y, row in enumerate(grid) for number in re.finditer(r"\d+", row)]

    result = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '*':
                continue

            connected_numbers = set()
            for check_x in range(max(0, x - 1), min(len(grid[0]), x + 2)):
                for check_y in range(max(0, y - 1), min(len(grid), y + 2)):
                    for num_y, num_start, num_end, num in numbers:
                        if num_start <= check_x < num_end and check_y == num_y:
                            connected_numbers.add(num)

            if len(connected_numbers) != 2:
                continue
            result += math.prod(connected_numbers)

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
