rows, cols, classes = map(int, input().split())

positions = [input() for _ in range(rows)]
pos_to_color = {positions[0][0]: 0}

for col in range(cols):
    color = col
    for row in range(rows):
        if positions[row][col] in pos_to_color:
            color = pos_to_color[positions[row][col]]
            break

    for row in range(rows):
        pos_to_color[positions[row][col]] = color

print(pos_to_color)

print(len(set(pos_to_color.values())))




