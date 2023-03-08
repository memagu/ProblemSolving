player_to_name = {'X': "Johan", 'O': "Abdullah"}

grid = [input().split() for _ in range(3)]

for i in range(3):
    player = grid[1][i]
    if player == '_':
        continue

    if player == grid[0][i] == grid[2][i]:
        print(f"{player_to_name[player]} har vunnit")
        quit()

for i in range(3):
    player = grid[i][1]
    if player == '_':
        continue

    if player == grid[i][0] == grid[i][2]:
        print(f"{player_to_name[player]} har vunnit")
        quit()

player = grid[1][1]

if player == '_':
    print("ingen har vunnit")
    quit()

if player == grid[0][0] == grid[2][2]:
    print(f"{player_to_name[player]} har vunnit")
    quit()

if player == grid[2][0] == grid[0][2]:
    print(f"{player_to_name[player]} har vunnit")
    quit()

print("ingen har vunnit")
