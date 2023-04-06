def part1():
    score_mapping = {"A X": 3 + 1,
                     "A Y": 6 + 2,
                     "A Z": 0 + 3,
                     "B X": 0 + 1,
                     "B Y": 3 + 2,
                     "B Z": 6 + 3,
                     "C X": 6 + 1,
                     "C Y": 0 + 2,
                     "C Z": 3 + 3}

    with open("data.in", "r") as f:
        return sum(score_mapping[line.strip()] for line in f.readlines())


def part2():
    score_mapping = {"A X": 0 + 3,
                     "A Y": 3 + 1,
                     "A Z": 6 + 2,
                     "B X": 0 + 1,
                     "B Y": 3 + 2,
                     "B Z": 6 + 3,
                     "C X": 0 + 2,
                     "C Y": 3 + 3,
                     "C Z": 6 + 1}

    with open("data.in", "r") as f:
        return sum(score_mapping[line.strip()] for line in f.readlines())


if __name__ == "__main__":
    print(part1())
    print(part2())