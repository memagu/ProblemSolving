from collections import deque


def part1():
    with open("data.in", 'r') as f:
        height_map = tuple(line for line in map(str.strip, f.readlines()))

    rows = len(height_map)
    cols = len(height_map[0])

    for row_index, row in enumerate(height_map):
        if 'S' in row:
            start_pos = row_index, row.index('S')

    scan_directions = ((-1, 0), (1, 0), (0, -1), (0, 1))  # (row_delta, col_delta)

    visited = {start_pos}
    queue = deque((start_pos,))
    depth = 0

    while queue:
        for _ in range(len(queue)):
            current_pos = queue.popleft()
            current_height = height_map[current_pos[0]][current_pos[1]]

            if current_height == 'E':
                queue.clear()
                break

            for row, col in ((current_pos[0] + direction[0], current_pos[1] + direction[1]) for direction in
                             scan_directions):
                if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols):
                    continue

                if ord(height_map[row][col]) - ord(current_height) > 1 and current_height != 'S':
                    continue

                if height_map[row][col] == 'E' and ord('z') - ord(current_height) > 1:
                    continue

                queue.append((row, col))
                visited.add((row, col))

            # print(current_height, current_pos, depth, queue, '\n')

        depth += 1

    return depth - 1


def part2():
    with open("data.in", 'r') as f:
        height_map = [line for line in map(str.strip, f.readlines())]

    rows = len(height_map)
    cols = len(height_map[0])

    starting_positions = []

    for row in range(rows):
        for col in range(cols):
            if height_map[row][col] not in ('a', 'S'):
                continue

            if height_map[row][col] == 'S':
                height_map[row] = height_map[row][:col] + 'a' + height_map[row][col + 1:]

            starting_positions.append((row, col))

    scan_directions = ((-1, 0), (1, 0), (0, -1), (0, 1))  # (row_delta, col_delta)

    shortest_path_length = float("inf")

    for start_pos in starting_positions:
        path_found = False

        visited = {start_pos}
        queue = deque((start_pos,))
        depth = 0

        while queue:
            for _ in range(len(queue)):
                current_pos = queue.popleft()
                current_height = height_map[current_pos[0]][current_pos[1]]

                if current_height == 'E':
                    path_found = True
                    queue.clear()
                    break

                for row, col in ((current_pos[0] + direction[0], current_pos[1] + direction[1]) for direction in
                                 scan_directions):
                    if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols):
                        continue

                    if ord(height_map[row][col]) - ord(current_height) > 1:
                        continue

                    if height_map[row][col] == 'E' and ord('z') - ord(current_height) > 1:
                        continue

                    queue.append((row, col))
                    visited.add((row, col))

                # print(current_height, current_pos, depth, queue, '\n')

            depth += 1

        if path_found:
            shortest_path_length = min(shortest_path_length, depth - 1)

    return shortest_path_length


if __name__ == "__main__":
    print(part1())
    print(part2())
