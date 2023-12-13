from functools import cache
from itertools import combinations


def part1():
    with open("data.in", 'r') as f:
        spring_data = [(springs, tuple(map(int, segments.split(',')))) for springs, segments in
                       map(str.split, f.read().splitlines())]

    result = 0
    for springs, segments in spring_data:
        unkown_broken = sum(segments) - springs.count('#')
        unkown = [i for i, spring in enumerate(springs) if spring == '?']

        arrangements = 0
        for permutation in combinations(unkown, unkown_broken):
            temp = list(springs)
            for i, spring in enumerate(springs):
                if spring == '?':
                    temp[i] = '#' if i in permutation else '.'

            segment_index = 0
            expected = []
            for spring in temp:
                if not expected:
                    if spring == '#':
                        if segment_index >= len(segments):
                            break
                        expected.extend('.' + '#' * (segments[segment_index] - 1))
                        segment_index += 1
                    continue

                if spring != expected.pop():
                    break
            else:
                arrangements += 1

        result += arrangements

    return result


def part2():
    @cache
    def arrangements(springs: str, counts: tuple[int]) -> int:
        if not springs:
            return len(counts) == 0

        if not counts:
            return "#" not in springs

        result = 0

        if springs[0] in ".?":
            result += arrangements(springs[1:], counts)

        if (springs[0] in "#?" and counts[0] <= len(springs) and "." not in springs[:counts[0]] and (counts[0] == len(springs) or springs[counts[0]] != "#")):
            result += arrangements(springs[counts[0] + 1:], counts[1:])

        return result

    with open("data.in", 'r') as f:
        spring_data = [('?'.join(springs for _ in range(5)), tuple(map(int, segments.split(','))) * 5) for springs, segments in
                       map(str.split, f.read().splitlines())]

    return sum(arrangements(springs, counts) for springs, counts in spring_data)


if __name__ == "__main__":
    print(part1())
    print(part2())
