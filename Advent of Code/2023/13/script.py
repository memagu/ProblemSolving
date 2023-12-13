def part1():
    with open("data.in", 'r') as f:
        patterns = [[]]
        for line in f.read().splitlines():
            if line:
                patterns[-1].append(line)
                continue

            patterns.append([])

    result = 0
    for pattern in patterns:
        horizontal = 0
        vertical = 0

        for i in range(1, len(pattern)):
            length = min(i, len(pattern) - i)
            if pattern[i - length:i] == pattern[i + length - 1:i - 1:-1]:
                horizontal = i
                break

        transposed_pattern = tuple(zip(*pattern))

        for i in range(1, len(transposed_pattern)):
            length = min(i, len(transposed_pattern) - i)
            if transposed_pattern[i - length:i] == transposed_pattern[i + length - 1:i - 1:-1]:
                vertical = i
                break

        result += vertical + 100 * horizontal

    return result


def part2():
    with open("data.in", 'r') as f:
        patterns = [[]]
        for line in f.read().splitlines():
            if line:
                patterns[-1].append(line)
                continue

            patterns.append([])

    result = 0
    for pattern in patterns:
        horizontal = 0
        vertical = 0

        for i in range(1, len(pattern)):
            length = min(i, len(pattern) - i)
            if pattern[i - length:i] == pattern[i + length - 1:i - 1:-1]:
                horizontal = i
                break

        transposed_pattern = tuple(zip(*pattern))

        for i in range(1, len(transposed_pattern)):
            length = min(i, len(transposed_pattern) - i)
            if transposed_pattern[i - length:i] == transposed_pattern[i + length - 1:i - 1:-1]:
                vertical = i
                break

        for row, line in enumerate(pattern):
            for col, char in enumerate(line):
                temp = pattern.copy()
                temp[row] = temp[row][:col] + ('.' if char == '#' else '#') + temp[row][col + 1:]

                new_horizontal = 0
                new_vertical = 0

                for i in range(1, len(temp)):
                    length = min(i, len(temp) - i)
                    if temp[i - length:i] == temp[i + length - 1:i - 1:-1]:
                        new_horizontal = i if i != horizontal else 0
                        if new_horizontal:
                            break

                transposed_temp = tuple(zip(*temp))

                for i in range(1, len(transposed_temp)):
                    length = min(i, len(transposed_temp) - i)
                    if transposed_temp[i - length:i] == transposed_temp[i + length - 1:i - 1:-1]:
                        new_vertical = i if i != vertical else 0
                        if new_vertical:
                            break

                if new_horizontal or new_vertical:
                    result += new_vertical + new_horizontal * 100
                    break
            else:
                continue
            break

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
