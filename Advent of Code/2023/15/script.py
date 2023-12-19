def part1():
    def _hash(s: str) -> int:
        result = 0
        for char in s:
            result += ord(char)
            result *= 17
            result %= 256

        return result

    with open("data.in", 'r') as f:
        instructions = f.read().strip().split(',')

    return sum(_hash(instruction) for instruction in instructions)


def part2():
    def _hash(s: str) -> int:
        result = 0
        for char in s:
            result += ord(char)
            result *= 17
            result %= 256

        return result

    with open("data.in", 'r') as f:
        instructions = f.read().strip().split(',')

    hashmap = [[] for _ in range(256)]

    for instruction in instructions:
        if '-' in instruction:
            label = instruction.removesuffix('-')
            label_hash = _hash(label)
            hashmap[label_hash] = [t for t in hashmap[label_hash] if t[0] != label]
            continue

        label, new_focal_length = instruction.split('=')
        label_hash = _hash(label)
        for i, (lens_label, _) in enumerate(hashmap[label_hash]):
            if lens_label == label:
                hashmap[label_hash][i] = (label, int(new_focal_length))
                break
        else:
            hashmap[label_hash].append((label, int(new_focal_length)))

    result = 0
    for box_number, box in enumerate(hashmap, 1):
        for slot_number, (_, focal_length) in enumerate(box, 1):
            result += box_number * slot_number * focal_length

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
