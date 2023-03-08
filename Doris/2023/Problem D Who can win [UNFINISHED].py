grid = [input().split() for _ in range(3)]

x_amount = 0
o_amount = 0
for row in grid:
    for char in row:
        if char == 'X':
            x_amount += 1

        elif char == 'O':
            o_amount += 1

rows = [set(row) for row in grid]
cols = [set(grid[i][j] for i in range(3)) for j in range(3)]
diagonals = [set(grid[i][i] for i in range(3)), set(set(grid[2 - i][i] for i in range(3)))]

johan_can_win = False
abdullah_can_win = False

all = rows + cols + diagonals

if {'X', '_'} in all:
    johan_can_win = x_amount < 6

if {'O', '_'} in all:
    abdullah_can_win = o_amount < 5

if {'_'} in all:
    johan_can_win = x_amount < 6
    abdullah_can_win = o_amount < 5

if johan_can_win and abdullah_can_win:
    print("Abdullah och Johan kan vinna")

if johan_can_win:
    print("Johan kan vinna")

if abdullah_can_win:
    print("Abdullahkan vinna")

print("ingen kan vinna")
