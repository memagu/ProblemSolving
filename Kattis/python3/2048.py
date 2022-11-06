grid = []
grid_size = 4

# Make grid
for i in range(grid_size):
    grid.append([[x, False] for x in list(map(int, input().split()))])

# Define directions
directions = {2: [0, -1], 3: [-1, 0], 0: [0, 1], 1: [1, 0]}
direction = directions[int(input())]

while True:
    # Copy grid
    last = []
    for i in range(grid_size):
        last.append([[x[0], x[1]] for x in grid[i]])

    # Loop through grid in selected direction
    for row in list(range(grid_size))[::(direction[0] if direction[0] != 0 else 1)]:
        for col in list(range(grid_size))[::(direction[1] if direction[1] != 0 else 1)]:

            curr = grid[row][col]

            # Check if "comp" will be inside the bounds of the grid
            if row + direction[0] not in [-1, grid_size] and col + direction[1] not in [-1, grid_size]:
                comp = grid[row + direction[0]][col + direction[1]]

                # Compare current tile with next tile in direction and then proceed accordingly
                if curr[0] + comp[0] != 0:
                    if (comp[0] in [curr[0], 0] or curr[0] == 0) and not (curr[1] or comp[1]):
                        grid[row][col] = [curr[0] + comp[0], comp[1]]
                        grid[row + direction[0]][col + direction[1]] = [0, False]

                        # Make the tile remember if it was merged
                        if (curr[0] == comp[0] and comp[0] != 0) or (curr[0] != 0 and comp[0] == curr[0]):
                            grid[row][col][1] = True

    # Break the while loop if no changes has been made to the grid compared to the previous iteration of the while loop
    if last == grid:
        break

# Print the grid
for r in grid:
    s_v = " ".join([str(t[0]) for t in r])
    print(s_v)
