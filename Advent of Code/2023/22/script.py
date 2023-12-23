from bisect import insort
from collections import defaultdict
from pprint import pprint
import sys



def part1():
    with open("data.in", 'r') as f:
        bricks = [((~sys.maxsize, ~sys.maxsize, -1), (sys.maxsize, sys.maxsize, -1))]
        for line in f.read().splitlines():
            (x1, y1, z1), (x2, y2, z2) = [map(int, coordinate.split(',')) for coordinate in line.split('~')]
            if z1 <= z2:
                bricks.append(((x1, y1, z1), (x2, y2, z2)))
            else:
                bricks.append(((x2, y2, z2), (x1, y1, z1)))

        bricks.sort(key=lambda coordinates: coordinates[0][2])

    compacted = []
    indices = {}
    for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
        max_height = -1
        stands_on = []
        for (x3, y3, z3), (x4, y4, z4), _, _ in compacted:
            minb1x, minb1y = min((x1, y1), (x2, y2))
            maxb1x, maxb1y = max((x1, y1), (x2, y2))
            minb2x, minb2y = min((x3, y3), (x4, y4))
            maxb2x, maxb2y = max((x3, y3), (x4, y4))

            if z2 < z3 or (maxb1x < minb2x or maxb2x < minb1x or maxb1y < minb2y or maxb2y < minb1y):
                continue

            if z4 < max_height:
                break

            max_height = z4
            stands_on.append(indices[((x3, y3, z3), (x4, y4, z4))])

        new_coordinate_bottom, new_coordinate_top = (x1, y1, max_height + 1), (x2, y2, z2 - z1 + max_height + 1)
        indices[(new_coordinate_bottom, new_coordinate_top)] = i
        insort(compacted, [new_coordinate_bottom, new_coordinate_top, True, stands_on],
               key=lambda brick_info: -brick_info[1][2])

    compacted.sort(key=lambda brick_info: indices[tuple(brick_info[:2])])

    for _, _, _, stands_on in compacted:
        if len(stands_on) == 1:
            compacted[stands_on[0]][2] = False

    return sum(brick_info[2] for brick_info in compacted)


def part2():
    with open("example.in", 'r') as f:
        bricks = [((~sys.maxsize, ~sys.maxsize, -1), (sys.maxsize, sys.maxsize, -1))]
        for line in f.read().splitlines():
            (x1, y1, z1), (x2, y2, z2) = [map(int, coordinate.split(',')) for coordinate in line.split('~')]
            if z1 <= z2:
                bricks.append(((x1, y1, z1), (x2, y2, z2)))
            else:
                bricks.append(((x2, y2, z2), (x1, y1, z1)))

        bricks.sort(key=lambda coordinates: coordinates[0][2])

    compacted = []
    indices = {}
    for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
        max_height = -1
        stands_on = []
        for (x3, y3, z3), (x4, y4, z4), _ in compacted:
            minb1x, minb1y = min((x1, y1), (x2, y2))
            maxb1x, maxb1y = max((x1, y1), (x2, y2))
            minb2x, minb2y = min((x3, y3), (x4, y4))
            maxb2x, maxb2y = max((x3, y3), (x4, y4))

            if z2 < z3 or (maxb1x < minb2x or maxb2x < minb1x or maxb1y < minb2y or maxb2y < minb1y):
                continue

            if z4 < max_height:
                break

            max_height = z4
            stands_on.append(indices[((x3, y3, z3), (x4, y4, z4))])

        new_coordinate_bottom, new_coordinate_top = (x1, y1, max_height + 1), (x2, y2, z2 - z1 + max_height + 1)
        indices[(new_coordinate_bottom, new_coordinate_top)] = i
        insort(compacted, [new_coordinate_bottom, new_coordinate_top, stands_on],
               key=lambda brick_info: -brick_info[1][2])

    compacted.sort(key=lambda brick_info: indices[tuple(brick_info[:2])])

    graph = defaultdict(lambda: (set(), set()))
    for i, (_, _, stands_on) in enumerate(compacted):
        graph[i][0].update(stands_on)
        for j in stands_on:
            graph[j][1].add(i)

    del graph[0]

    pprint(graph)

    max_disintegrated = 0
    for start in graph:
        disintegrated = 0
        queue = [start]
        visited = {start,}
        while queue:
            parents, children = graph[queue.pop()]

            if len(parents) > 1 and (parents - visited):
                continue

            disintegrated += 1

            queue.extend(children)
            visited.update(children)

        max_disintegrated = max(max_disintegrated, disintegrated)

    return max_disintegrated

    # TODO mark extendible tree





if __name__ == "__main__":
    print(part1())
    print(part2())
