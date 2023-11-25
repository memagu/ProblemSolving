from typing import Tuple


class DisjointSet:
    def __init__(self):
        self.elements = {}

    def find(self, element: Tuple[int, int]) -> Tuple[int, int]:
        if element not in self.elements:
            self.elements[element] = {"parent": element, "rank": 0, "area": 1}
            return element

        if self.elements[element]["parent"] != element:
            self.elements[element]["parent"] = self.find(self.elements[element]["parent"])

        return self.elements[element]["parent"]

    def union(self, element_1: Tuple[int, int], element_2: Tuple[int, int]) -> None:
        parent_1, parent_2 = self.find(element_1), self.find(element_2)
        if parent_1 == parent_2:
            return

        if self.elements[parent_1]["rank"] > self.elements[parent_2]["rank"]:
            parent_1, parent_2 = parent_2, parent_1

        if self.elements[parent_1]["rank"] == self.elements[parent_2]["rank"]:
            self.elements[parent_2]["rank"] += 1

        self.elements[parent_1]["parent"] = parent_2
        self.elements[parent_2]["area"] += self.elements[parent_1]["area"]


n_rows, n_cols, n_updates = map(int, (input() for _ in range(3)))
image = [input() for _ in range(n_rows)]
disjoint_set = DisjointSet()

start = None
for x in range(n_cols):
    for y in range(n_rows):
        symbol = image[y][x]

        if symbol == '.':
            continue

        if symbol == 'S':
            start = (x, y)

        for dx, dy in ((1, 0), (0, 1)):
            nx, ny = x + dx, y + dy
            if nx < n_cols and ny < n_rows and image[ny][nx] != '.':
                disjoint_set.union((x, y), (nx, ny))

print(disjoint_set.elements[disjoint_set.find(start)]["area"])

new_nodes = set()
for y, x in (map(lambda c: int(c) - 1, input().split()) for _ in range(n_updates)):
    new_nodes.add((x, y))

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n_cols and 0 <= ny < n_rows and ((nx, ny) in new_nodes or image[ny][nx] != '.'):
            disjoint_set.union((x, y), (nx, ny))

    print(disjoint_set.elements[disjoint_set.find(start)]["area"])
