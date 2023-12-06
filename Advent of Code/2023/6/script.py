import math

def part1():
    with open("data.in", 'r') as f:
        times, distance_records = (tuple(map(int, line.strip().split()[1:])) for line in f.readlines())

    return math.prod(sum(button_time * (max_time - button_time) > distance_record for button_time in range(max_time)) for max_time, distance_record in zip(times, distance_records))


def part2():
    with open("data.in", 'r') as f:
        max_time, distance_record = (int(''.join(line.strip().split()[1:])) for line in f.readlines())

    return sum(button_time * (max_time - button_time) > distance_record for button_time in range(max_time))


if __name__ == "__main__":
    print(part1())
    print(part2())
