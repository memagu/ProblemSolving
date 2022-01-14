grid = []
for i in range(4):
    grid.append([[x, False] for x in list(map(int, input().split()))])

directions = {2: [0, -1], 3: [-1, 0], 0: [0, 1], 1: [1, 0]}
direction = directions[int(input())]


move = True
while move:
    move = False
    last = []
    for i in range(4):
        last.append([[x[0], x[1]] for x in grid[i]])

    for row in list(range(4))[::(direction[0] if direction[0] != 0 else 1)]:
        for col in list(range(4))[::(direction[1] if direction[1] != 0 else 1)]:

            curr = grid[row][col]

            if row + direction[0] not in [-1, 4] and col + direction[1] not in [-1, 4]:
                comp = grid[row + direction[0]][col + direction[1]]

                if curr[0] + comp[0] != 0:
                    if (comp[0] in [curr[0], 0] or curr[0] == 0) and not (curr[1] or comp[1]):
                        grid[row][col] = [curr[0] + comp[0], comp[1]]
                        grid[row + direction[0]][col + direction[1]] = [0, False]
                        move = True

                        if (curr[0] == comp[0] and comp[0] != 0) or (curr[0] != 0 and comp[0] == curr[0]):
                            grid[row][col][1] = True

    if last == grid:
        move = False

for r in grid:
    s_v = " ".join([str(t[0]) for t in r])
    print(s_v)
