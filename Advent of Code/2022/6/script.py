def part1():
    with open("data.in", 'r') as f:
        buffer = f.read()

    for i in range(len(buffer) - 4):
        if len(set(buffer[i:i + 4])) == 4:
            return i + 4


def part2():
    with open("data.in", 'r') as f:
        buffer = f.read()

    for i in range(len(buffer) - 14):
        if len(set(buffer[i:i + 14])) == 14:
            return i+14


if __name__ == "__main__":
    print(part1())
    print(part2())
