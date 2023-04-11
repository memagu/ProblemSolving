"""
If both values are integers, the lower integer should come first. If the left integer is lower than the right integer
the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the
right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.

If both values are lists, compare the first value of each list, then the second value, and so on. If the left list
runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are
not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue
checking the next part of the input.

If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then
retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2);
the result is then found by instead comparing [0,0,0] and [2].
"""

from functools import cmp_to_key


def compare(left, right):
    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]

    for left_2, right_2 in zip(left, right):
        if isinstance(left_2, list) or isinstance(right_2, list):
            result = compare(left_2, right_2)
        else:
            result = right_2 - left_2

        if result != 0:
            return result

    return len(right) - len(left)


def part1():
    pairs = [[]]

    with open("data.in", 'r') as f:
        for i, line in enumerate(map(str.strip, f.readlines()), 1):
            if i % 3 == 0:
                pairs.append([])
                continue

            pairs[-1].append(eval(line))

    return sum(i for i, (left, right) in enumerate(pairs, 1) if compare(left, right) > 0)


def part2():
    with open("data.in", 'r') as f:
        packets = [eval(line.strip()) for i, line in enumerate(f.readlines(), 1) if i % 3] + [[[2]], [[6]]]

    packets.sort(key=cmp_to_key(compare), reverse=True)

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == "__main__":
    print(part1())
    print(part2())