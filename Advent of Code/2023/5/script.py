from collections import deque


def part1():
    with open("data.in", 'r') as f:
        lines = iter(f.read().splitlines())

    seeds = map(int, next(lines).split()[1:])

    maps = {}
    current_map = ''
    for line in lines:
        if line.endswith("map:"):
            current_map = line.split()[0]
            maps[current_map] = []
            continue

        if line:
            destination_start, source_start, range_length = map(int, line.split())
            maps[current_map].append((destination_start, range(source_start, source_start + range_length)))

    conversion_step = "seed-to-soil"

    queue = deque(seeds)
    while True:
        for _ in range(len(queue)):
            value = queue.popleft()
            for destination_start, source_range in maps[conversion_step]:
                if value in source_range:
                    queue.append(destination_start + value - source_range.start)
                    break
            else:
                queue.append(value)

        next_map = conversion_step.split('-')[-1]

        if next_map == "location":
            break

        conversion_step = next((map_name for map_name in maps if map_name.startswith(next_map)))

    return min(queue)


def part2():
    with open("data.in", 'r') as f:
        lines = iter(f.read().splitlines())

    seeds = tuple(map(int, next(lines).split()[1:]))
    seed_ranges = [range(start, start + length) for start, length in zip(seeds[::2], seeds[1::2])]

    maps = {}
    current_map = ''
    for line in lines:
        if line.endswith("map:"):
            current_map = line.split()[0]
            maps[current_map] = []
            continue

        if line:
            destination_start, source_start, range_length = map(int, line.split())
            maps[current_map].append((range(source_start, source_start + range_length), destination_start - source_start))

    for map_name, conversions in maps.items():
        maps[map_name] = sorted(conversions, key=lambda t: t[0].start)

    conversion_step = "seed-to-soil"

    queue = deque(seed_ranges)
    while True:
        for _ in range(len(queue)):
            seed_range = queue.popleft()
            for source_range, diff in maps[conversion_step]:
                before = range(seed_range.start, min(seed_range.stop, source_range.start))
                inside = range(max(seed_range.start, source_range.start), min(seed_range.stop, source_range.stop))
                after = range(max(seed_range.start, source_range.stop), seed_range.stop)

                if before:
                    queue.append(before)
                if inside:
                    queue.append(range(inside.start + diff, inside.stop + diff))
                if after:
                    seed_range = after
                else:
                    break
            else:
                queue.append(seed_range)

        next_map = conversion_step.split('-')[-1]

        if next_map == "location":
            break

        conversion_step = next((map_name for map_name in maps if map_name.startswith(next_map)))

    return min(queue, key=lambda r: r.start).start


if __name__ == "__main__":
    print(part1())
    print(part2())
