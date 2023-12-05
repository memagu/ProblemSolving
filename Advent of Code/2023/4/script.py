def part1():
    with open("data.in", 'r') as f:
        lines = f.read().splitlines()

    result = 0
    for line in lines:
        card, winning = [set(map(int, card.split())) for card in line.split(": ")[1].split(" | ")]
        common = card.intersection(winning)
        if common:
            result += 1 << (len(card.intersection(winning)) - 1)

    return result


def part2():
    with open("data.in", 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    card_counts = [1] * len(lines)
    for game, line in enumerate(lines):
        card, winning = [set(map(int, card.split())) for card in line.split(": ")[1].split(" | ")]
        common = card.intersection(winning)
        if common:
            for i in range(game + 1, game + 1 + len(common)):
                card_counts[i] += card_counts[game]

    return sum(card_counts)


if __name__ == "__main__":
    print(part1())
    print(part2())
