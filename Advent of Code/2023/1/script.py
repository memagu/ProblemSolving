def part1():
    with open("data.in", 'r') as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        for char in line:
            if char.isdigit():
                result += 10 * int(char)
                break

        for char in reversed(line):
            if char.isdigit():
                result += int(char)
                break

    return result


def part2():
    str_to_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    with open("data.in", 'r') as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        for i, char in enumerate(line):
            if char.isdigit():
                result += 10 * int(char)
                break

            for strnum in str_to_int:
                if line[i:i + len(strnum)] == strnum:
                    result += 10 * str_to_int[strnum]
                    break
            else:
                continue

            break

        for i, char in enumerate(reversed(line)):
            i = -i + -1
            if char.isdigit():
                result += int(char)
                break

            for strnum in str_to_int:
                if line[i - len(strnum):i] == strnum:
                    result += str_to_int[strnum]
                    break
            else:
                continue

            break

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
