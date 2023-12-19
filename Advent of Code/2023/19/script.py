from functools import partial, reduce
from math import prod
from operator import gt, lt
import re


def part1():
    with open("data.in", 'r') as f:
        workflows_raw, parts_raw = f.read().split("\n\n")

        workflows = {}
        for line in workflows_raw.split('\n'):
            workflow_name, operations = re.match(r"(.+)\{(.+)}", line).groups()
            operations = operations.split(',')

            workflow_operations = []
            for operation in operations[:-1]:
                key, comparison, value, destination = re.match(r"([xmas])([<>])(\d+):(.+)", operation).groups()
                workflow_operations.append((key, partial(gt if comparison == '<' else lt, int(value)), destination))

            workflow_operations.append(('x', lambda _: True, operations[-1]))

            workflows[workflow_name] = workflow_operations

        parts = []
        for line in parts_raw.split('\n'):
            parts.append({key: value for key, value in
                          zip("xmas", map(int, re.match(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line).groups()))})

    result = 0
    for part in parts:
        workflow = workflows['in']
        done = False
        while not done:
            for key, comparison, destination in workflow:
                if not comparison(part[key]):
                    continue

                if destination in 'AR':
                    if destination == 'A':
                        result += sum(part.values())
                    done = True

                else:
                    workflow = workflows[destination]

                break

    return result


def part2():
    with open("data.in", 'r') as f:
        workflows = {}
        for line in f.read().split("\n\n")[0].split('\n'):
            workflow_name, operations = re.match(r"(.+)\{(.+)}", line).groups()
            operations = operations.split(',')

            workflow_operations = []
            for operation in operations[:-1]:
                key, comparison, value, destination = re.match(r"([xmas])([<>])(\d+):(.+)", operation).groups()
                workflow_operations.append((key, comparison, int(value), destination))

            workflow_operations.append((None, None, None, operations[-1]))

            workflows[workflow_name] = workflow_operations

    result = 0
    queue = [('in', {key: range(1, 4001) for key in "xmas"})]

    while queue:
        workflow_name, value_ranges = queue.pop()
        if workflow_name in 'AR':
            if workflow_name == 'A':
                result += prod(map(len, value_ranges.values()))
            continue

        for key, operation, comparison_value, destination in workflows[workflow_name]:
            if operation is None:
                queue.append((destination, value_ranges))
                break

            old_range = value_ranges[key]
            new_value_ranges = value_ranges.copy()

            if operation == '>':
                new_value_ranges[key] = range(max(old_range.start, comparison_value + 1), old_range.stop)
                value_ranges[key] = range(old_range.start, min(old_range.stop, comparison_value + 1))
            else:
                new_value_ranges[key] = range(old_range.start, min(old_range.stop, comparison_value))
                value_ranges[key] = range(max(old_range.start, comparison_value), old_range.stop)

            queue.append((destination, new_value_ranges))

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
