import string


def part1():
    result = 0

    with open("data.in", "r") as f:
        for line in f.readlines():
            line = line.strip()
            compartment_1 = set()
            compartment_2 = set()

            offset = len(line) >> 1
            for i in range(offset):
                compartment_1.add(line[i])
                compartment_2.add(line[i + offset])

            item = compartment_1.intersection(compartment_2).pop()

            if item in string.ascii_lowercase:
                result += ord(item) - 96
                continue

            result += ord(item) - 38

    return result


def part2():
    result = 0

    with open("data.in", "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            elf_index = i % 3

            if elf_index == 0:
                items = set(line)
                continue

            items = items.intersection(set(line))

            if elf_index == 2:
                item = items.pop()

                if item in string.ascii_lowercase:
                    result += ord(item) - 96
                    continue

                result += ord(item) - 38

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
