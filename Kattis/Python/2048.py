grid = []
for i in range(4):
    grid.append(list(map(int, input().split())))

directions = {0: [0, -1], 1: [-1, 0], 2: [0, 1], 3: [1, 0]}
direction = directions[int(input())]

for i in range(2):
    for row in list(range(4))[::(direction[0] if direction[0] != 0 else 1)]:
        for col in list(range(4))[::(direction[1] if direction[1] != 0 else 1)]:
            curr = grid[row][col]
            if row + direction[0] not in [-1, 4] and col + direction[1] not in [-1, 4] and curr != 0:
                comp = grid[row + direction[0]][col + direction[1]]
                if comp in [curr, 0]:
                    #print(f"row: {row}, col: {col}, value: {grid[row][col]}")
                    grid[row + direction[0]][col + direction[1]] += curr
                    grid[row][col] = 0


for row in grid:
    print(row)

