from collections import Counter, defaultdict
import bisect


def part1():
    denominations = {denomination: i for i, denomination in enumerate("AKQJT98765432")}

    with open("data.in", 'r') as f:
        lines = [(hand, int(bet)) for hand, bet in map(str.split, f.read().splitlines())]

    hands = defaultdict(list)
    for hand, bet in lines:
        match Counter(hand).most_common(2):
            case [(_, 5)]:
                hand_type = "five_of_a_kind"
            case [(_, 4), _]:
                hand_type = "four_of_a_kind"
            case [(_, 3), (_, 2)]:
                hand_type = "full_house"
            case [(_, 3), _]:
                hand_type = "three_of_a_kind"
            case [(_, 2), (_, 2)]:
                hand_type = "two_pair"
            case [(_, 2), _]:
                hand_type = "one_pair"
            case _:
                hand_type = "high_card"

        bisect.insort(hands[hand_type], (hand, bet), key=lambda t: tuple(denominations[denomination] for denomination in t[0]))

    result = 0
    multiplier = len(lines)
    for hand_type in (
    "five_of_a_kind", "four_of_a_kind", "full_house", "three_of_a_kind", "two_pair", "one_pair", "high_card"
    ):
        if not hand_type in hands:
            continue

        for _, bet in hands[hand_type]:
            result += bet * multiplier
            multiplier -= 1

    return result


def part2():
    denominations = {denomination: i for i, denomination in enumerate("AKQT98765432J")}

    with open("data.in", 'r') as f:
        lines = [(hand, int(bet)) for hand, bet in map(str.split, f.read().splitlines())]

    hands = defaultdict(list)
    for hand, bet in lines:
        match hand.count('J'):
            case 0:
                match Counter(hand.replace('J', '')).most_common(2):
                    case [(_, 5)]:
                        hand_type = "five_of_a_kind"
                    case [(_, 4), _]:
                        hand_type = "four_of_a_kind"
                    case [(_, 3), (_, 2)]:
                        hand_type = "full_house"
                    case [(_, 3), _]:
                        hand_type = "three_of_a_kind"
                    case [(_, 2), (_, 2)]:
                        hand_type = "two_pair"
                    case [(_, 2), _]:
                        hand_type = "one_pair"
                    case _:
                        hand_type = "high_card"
            case 1:
                match Counter(hand.replace('J', '')).most_common(2):
                    case [(_, 4)]:
                        hand_type = "five_of_a_kind"
                    case [(_, 3), _]:
                        hand_type = "four_of_a_kind"
                    case [(_, 2), (_, 2)]:
                        hand_type = "full_house"
                    case [(_, 2), _]:
                        hand_type = "three_of_a_kind"
                    case _:
                        hand_type = "one_pair"
            case 2:
                match Counter(hand.replace('J', '')).most_common(2):
                    case [(_, 3)]:
                        hand_type = "five_of_a_kind"
                    case [(_, 2), _]:
                        hand_type = "four_of_a_kind"
                    case _:
                        hand_type = "three_of_a_kind"
            case 3:
                match Counter(hand.replace('J', '')).most_common(2):
                    case [(_, 2)]:
                        hand_type = "five_of_a_kind"
                    case _:
                        hand_type = "four_of_a_kind"
            case _:
                hand_type = "five_of_a_kind"

        bisect.insort(hands[hand_type], (hand, bet),
                      key=lambda t: tuple(denominations[denomination] for denomination in t[0]))

    result = 0
    multiplier = len(lines)
    for hand_type in (
            "five_of_a_kind", "four_of_a_kind", "full_house", "three_of_a_kind", "two_pair", "one_pair", "high_card"
    ):
        if not hand_type in hands:
            continue

        for _, bet in hands[hand_type]:
            result += bet * multiplier
            multiplier -= 1

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
