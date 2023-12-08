import re
import math

def part1():
    with open("data.in", 'r') as f:
        instructions = f.readline().strip()
        f.readline()
        graph = {}
        for line in f.read().splitlines():
            node, left, right = re.search(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line).groups()
            graph[node] = (left, right)

    step = 0
    node = "AAA"
    while node != "ZZZ":
        match instructions[step % len(instructions)]:
            case 'L':
                node = graph[node][0]
            case 'R':
                node = graph[node][1]

        step += 1

    return step

def part2():
    with open("data.in", 'r') as f:
        instructions = f.readline().strip()
        f.readline()
        graph = {}
        for line in f.read().splitlines():
            node, left, right = re.search(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line).groups()
            graph[node] = (left, right)

    steps = set()
    for node in (node for node in graph if node.endswith('A')):
        step = 0
        while not node.endswith('Z'):
            match instructions[step % len(instructions)]:
                case 'L':
                    node = graph[node][0]
                case 'R':
                    node = graph[node][1]

            step += 1

        steps.add(step)

    return math.lcm(*steps)



if __name__ == "__main__":
    print(part1())
    print(part2())
