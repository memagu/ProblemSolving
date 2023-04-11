from collections import deque
from dataclasses import dataclass
from functools import reduce
from typing import List


@dataclass
class Monkey:
    items: deque[int]
    operation: str
    test: int
    on_passed: int
    on_failed: int
    number_of_inspections: int = 0


def part1():
    monkeys: List[Monkey] = []

    with open("data.in", 'r') as f:
        while f.readline().startswith("Monkey"):
            items = deque(map(int, f.readline().strip().split(maxsplit=2)[2].split(", ")))
            operation = ' '.join(f.readline().strip().split()[3:]).replace("old", "item")
            test = int(f.readline().strip().split()[3])
            on_passed = int(f.readline().strip().split()[5])
            on_failed = int(f.readline().strip().split()[5])

            monkeys.append(Monkey(items, operation, test, on_passed, on_failed))

            _ = f.readline()

    for _ in range(20):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                monkey.number_of_inspections += 1
                item = monkey.items.popleft()
                item = eval(monkey.operation) // 3

                if not item % monkey.test:
                    monkeys[monkey.on_passed].items.append(item)
                    continue

                monkeys[monkey.on_failed].items.append(item)

    most_active = sorted(monkeys, key=lambda monkey: monkey.number_of_inspections, reverse=True)[:2]
    return most_active[0].number_of_inspections * most_active[1].number_of_inspections


def part2():
    monkeys: list[Monkey] = []

    with open("data.in", 'r') as f:
        while f.readline().startswith("Monkey"):
            items = deque(map(int, f.readline().strip().split(maxsplit=2)[2].split(", ")))
            operation = ' '.join(f.readline().strip().split()[3:]).replace("old", "item")
            test = int(f.readline().strip().split()[3])
            on_passed = int(f.readline().strip().split()[5])
            on_failed = int(f.readline().strip().split()[5])

            monkeys.append(Monkey(items, operation, test, on_passed, on_failed))

            _ = f.readline()

    mod_product = reduce(lambda a, b: a * b, (monkey.test for monkey in monkeys))

    for i in range(10000):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                monkey.number_of_inspections += 1
                item = monkey.items.popleft()
                item = eval(monkey.operation)

                next_monkey = monkey.on_failed
                if not item % monkey.test:
                    next_monkey = monkey.on_passed

                monkeys[next_monkey].items.append(item % mod_product)

    most_active = sorted(monkeys, key=lambda monkey: monkey.number_of_inspections, reverse=True)[:2]
    return most_active[0].number_of_inspections * most_active[1].number_of_inspections


if __name__ == "__main__":
    print(part1())
    print(part2())
