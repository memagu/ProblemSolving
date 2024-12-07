from pathlib import Path


def part1(file: Path) -> int:
    with open(file, "r") as f:
        pass


def part2(file: Path) -> int:
    with open(file, "r") as f:
        pass


if __name__ == "__main__":
    example_path = Path("./example.in")
    data_path = Path("./data.in")

    print(f"Part 1: {part1(data_path)}")
    print(f"Part 1 (example): {part1(example_path)}")
    print(f"Part 2: {part2(data_path)}")
    print(f"Part 2 (example): {part2(example_path)}")
