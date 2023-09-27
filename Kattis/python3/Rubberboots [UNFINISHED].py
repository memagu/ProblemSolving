from collections import defaultdict

n = input()
path = input().split()

graph = defaultdict(set)
edges = set()

direction = (0, 1)
position = (0, 0)

left_turn = ((0, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
right_turn = ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 1))
direction_instructions = {'U', '<', '>'}
last_instruction_was_direction_change = False
position_change = 0

for instruction in path:
    if instruction not in direction_instructions:
        last_instruction_was_direction_change = False
        position_change += int(instruction)
        continue

    if not last_instruction_was_direction_change:
        last_instruction_was_direction_change = True

        new_position = (position[0] + direction[0] * position_change, position[1] + direction[1] * position_change)
        graph[position].add((new_position, position_change - 1))
        graph[new_position].add((position, position_change - 1))
        edges.add((position, new_position))
        position = new_position
        position_change = 0

    if instruction == 'U':
        direction = (direction[0] * -1, direction[1] * -1)
        continue

    if instruction == '<':
        direction = left_turn[left_turn.index(direction) + 1]
        continue

    if instruction == '>':
        direction = right_turn[right_turn.index(direction) + 1]
        continue

new_position = (position[0] + direction[0] * position_change, position[1] + direction[1] * position_change)
graph[position].add((new_position, position_change - 1))
graph[new_position].add((position, position_change - 1))
edges.add((position, new_position))


print(graph, edges, sep='\n')