import math


def part1():
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    with open("data.in", 'r') as f:
        return sum(
            int(game.split()[-1]) for line in f.readlines() for game, game_rounds in (line.strip().split(": "),) if all(
                int(amount) <= max_cubes[color] for game_round in game_rounds.split("; ") for amount, color in
                (showcase.split() for showcase in game_round.split(", "))))


def part2():
    with open("data.in", 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    result = 0
    for line in lines:
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        game, game_rounds = line.split(": ")
        for amount, color in (showcase.split() for game_round in game_rounds.split("; ") for showcase in game_round.split(", ")):
            max_cubes[color] = max(max_cubes[color], int(amount))
        result += math.prod(max_cubes.values())

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
