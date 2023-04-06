def part1():
    elves = [0]

    with open("data.in", "r") as f:
        for line in f.readlines():
            line = line.strip()

            if not line:
                elves.append(0)
                continue

            elves[-1] += int(line)

    return max(elves)


def part2():
    elves = [0]

    with open("data.in", "r") as f:
        for line in f.readlines():
            line = line.strip()

            if not line:
                elves.append(0)
                continue

            elves[-1] += int(line)

    return sum(sorted(elves)[-3::])


if __name__ == "__main__":
    print(part1())
    print(part2())

    open()

