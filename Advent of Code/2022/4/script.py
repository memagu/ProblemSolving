def part1():
    with open("data.in", "r") as f:
        # return sum(int(elf_ranges[0][0] <= elf_ranges[1][0] and elf_ranges[0][1] >= elf_ranges[1][1] or elf_ranges[0][0] >= elf_ranges[1][0] and elf_ranges[0][1] <= elf_ranges[1][1]) for elf_ranges in (tuple(tuple(map(int, elf.split('-'))) for elf in line.strip().split(',')) for line in f.readlines()))

        counter = 0

        for line in f.readlines():
            elf_ranges = tuple(tuple(map(int, elf.split('-'))) for elf in line.strip().split(','))

            counter += int(elf_ranges[0][0] <= elf_ranges[1][0] and elf_ranges[0][1] >= elf_ranges[1][1] or elf_ranges[0][0] >= elf_ranges[1][0] and elf_ranges[0][1] <= elf_ranges[1][1])

        return counter


def part2():
    with open("data.in", "r") as f:
        return sum(int(elf_ranges[1][0] <= elf_ranges[0][0] <= elf_ranges[1][1] or elf_ranges[1][0] <= elf_ranges[0][1] <= elf_ranges[1][1] or elf_ranges[0][0] <= elf_ranges[1][0] <= elf_ranges[0][1] or elf_ranges[0][0] <= elf_ranges[1][1] <= elf_ranges[0][1]) for elf_ranges in (tuple(tuple(map(int, elf.split('-'))) for elf in line.strip().split(',')) for line in f.readlines()))

        counter = 0

        for line in f.readlines():
            elf_ranges = tuple(tuple(map(int, elf.split('-'))) for elf in line.strip().split(','))

            counter += int(elf_ranges[1][0] <= elf_ranges[0][0] <= elf_ranges[1][1] or elf_ranges[1][0] <= elf_ranges[0][1] <= elf_ranges[1][1] or elf_ranges[0][0] <= elf_ranges[1][0] <= elf_ranges[0][1] or elf_ranges[0][0] <= elf_ranges[1][1] <= elf_ranges[0][1])

        return counter


if __name__ == "__main__":
    print(part1())
    print(part2())
