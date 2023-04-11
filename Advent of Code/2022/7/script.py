from collections import deque


def part1():
    path_stack = ['/']
    filesystem = {'/': [0, set()]}

    with open("data.in", 'r') as f:
        for line in map(str.strip, f.readlines()):
            if line == "$ ls":
                continue

            if line.startswith("dir"):
                filesystem[''.join(path_stack) + line.split()[-1]] = [0, set()]
                continue

            if line.startswith("$ cd"):
                argument = line.split()[-1]

                if argument == "..":
                    path_stack.pop()
                    continue

                if argument == '/':
                    path_stack = ['/']
                    continue

                path_stack.append(argument)
                continue

            for i, directory in enumerate(path_stack):
                path = ''.join(path_stack[:i + 1])

                if i != len(path_stack) - 1:
                    filesystem[path][1].add(''.join(path_stack[:i + 2]))

                filesystem[path][0] += int(line.split()[0])

    return sum(size for size in map(lambda x: x[0], filesystem.values()) if size <= 100_000)


def part2():
    path_stack = ['/']
    filesystem = {'/': [0, set()]}

    with open("data.in", 'r') as f:
        for line in map(str.strip, f.readlines()):
            if line == "$ ls":
                continue

            if line.startswith("dir"):
                filesystem[''.join(path_stack) + line.split()[-1]] = [0, set()]
                continue

            if line.startswith("$ cd"):
                argument = line.split()[-1]

                if argument == "..":
                    path_stack.pop()
                    continue

                if argument == '/':
                    path_stack = ['/']
                    continue

                path_stack.append(argument)
                continue

            for i, directory in enumerate(path_stack):
                path = ''.join(path_stack[:i + 1])

                if i != len(path_stack) - 1:
                    filesystem[path][1].add(''.join(path_stack[:i + 2]))

                filesystem[path][0] += int(line.split()[0])

        required_space = filesystem['/'][0] - 40_000_000

        queue = deque(['/'])
        result = float('inf')

        while queue:
            any_larger_than_required = False
            for _ in range(len(queue)):
                size, subdirectories = filesystem[queue.popleft()]
                if size >= required_space:
                    any_larger_than_required = True
                    result = min(result, size)

                for subdirectory in subdirectories:
                    queue.append(subdirectory)

            if not any_larger_than_required:
                return result


if __name__ == "__main__":
    print(part1())
    print(part2())
