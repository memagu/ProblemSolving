from collections import defaultdict


def part1():
    with open("data.in", 'r') as f:
        graph = defaultdict(set)
        for line in f.read().splitlines():
            node, neighbours = line.split(": ")
            for neighbour in neighbours.split():
                graph[node].add(neighbour)
                graph[neighbour].add(node)

    island = set(graph)
    while sum(len(graph[node] - island) for node in island) != 3:  # while bridges != 3
        island.remove(max(
            island,
            key=lambda node: len(graph[node] - island)
        ))  # remove the node with most inter-island connections

    return len(island) * len(set(graph) - island)


def part2():
    return


if __name__ == "__main__":
    print(part1())
    print(part2())
