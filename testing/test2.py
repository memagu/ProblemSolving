class Tile:
    def __init__(self, value):
        self.value = value
        self.combined = False

    def __str__(self):
        return str(self.value)




grid = []
for i in range(4):
    grid.append([Tile(x) for x in list(map(int, input().split()))])


directions = {0: [0, -1], 1: [-1, 0], 2: [0, 1], 3: [1, 0]}
direction = directions[int(input())]

move = True
while move:
    move = False
    for row in list(range(4))[::(direction[0] if direction[0] != 0 else 1)]:
        for col in list(range(4))[::(direction[1] if direction[1] != 0 else 1)]:
            curr = grid[row][col]
            if row + direction[0] not in [-1, 4] and col + direction[1] not in [-1, 4] and curr != 0:
                comp = grid[row + direction[0]][col + direction[1]]
                if comp.value in [curr.value, 0] and not comp.combined:
                    move = True
                    comp.combined = True
                    #print(f"row: {row}, col: {col}, value: {grid[row][col]}")
                    comp.value += curr.value
                    curr.value = 0


for row in grid:
    s = " ".join([str(t) for t in row])
    print(s)