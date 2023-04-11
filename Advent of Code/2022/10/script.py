def part1():
    with open("data.in", 'r') as f:
        cycle = 0
        accumulated_value = 1
        get_signal_strength_at = {20, 60, 100, 140, 180, 220}
        result = 0

        for line in map(str.strip, f.readlines()):
            for i in range(2):
                cycle += 1

                if cycle in get_signal_strength_at:
                    result += cycle * accumulated_value

                if line == "noop":
                    break

                value = int(line.split()[1])
                accumulated_value += value * i

        return result


def part2():
    with open("data.in", 'r') as f:
        cycle = 0
        accumulated_value = 1
        result = ""

        for line in map(str.strip, f.readlines()):
            for i in range(2):
                cycle += 1

                result += ('#' if accumulated_value - 1 <= (cycle - 1) % 40 <= accumulated_value + 1 else '.') + (
                    '\n' if not cycle % 40 else '')

                if line == "noop":
                    break

                value = int(line.split()[1])
                accumulated_value += value * i

        return result


if __name__ == "__main__":
    print(part1())
    print(part2())
