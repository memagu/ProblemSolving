# https://open.kattis.com/problems/npuzzle

# 0.05s
# original_pos = {}
# letter = 65
# for cols in range(4):
#     for rows in range(4):
#         original_pos[chr(letter)] = [rows, cols]
#         letter += 1
#
# print(original_pos)
#
# input_pos = {}
# for i in range(4):
#     string_in = input()
#     input_pos[string_in[0]] = [0, i]
#     input_pos[string_in[1]] = [1, i]
#     input_pos[string_in[2]] = [2, i]
#     input_pos[string_in[3]] = [3, i]
#
# result = 0
#
# for key in input_pos:
#     if not key == ".":
#         orig_x, orig_y = original_pos[key]
#         in_x, in_y = input_pos[key]
#         result += abs(orig_x - in_x) + abs(orig_y - in_y)
#
# print(result)


# 0.05s
# original_pos = {'A': [0, 0], 'B': [1, 0], 'C': [2, 0], 'D': [3, 0], 'E': [0, 1], 'F': [1, 1], 'G': [2, 1], 'H': [3, 1], 'I': [0, 2], 'J': [1, 2], 'K': [2, 2], 'L': [3, 2], 'M': [0, 3], 'N': [1, 3], 'O': [2, 3], 'P': [3, 3]}
#
# input_pos = {}
# for i in range(4):
#     string_in = input()
#     input_pos[string_in[0]] = [0, i]
#     input_pos[string_in[1]] = [1, i]
#     input_pos[string_in[2]] = [2, i]
#     input_pos[string_in[3]] = [3, i]
#
# result = 0
#
# for key in input_pos:
#     if not key == ".":
#         orig_x, orig_y = original_pos[key]
#         in_x, in_y = input_pos[key]
#         result += abs(orig_x - in_x) + abs(orig_y - in_y)
#
# print(result)


# 0.05s
# original_pos = {'A': [0, 0], 'B': [1, 0], 'C': [2, 0], 'D': [3, 0], 'E': [0, 1], 'F': [1, 1], 'G': [2, 1], 'H': [3, 1], 'I': [0, 2], 'J': [1, 2], 'K': [2, 2], 'L': [3, 2], 'M': [0, 3], 'N': [1, 3], 'O': [2, 3]}
# result = 0
#
# for i in range(4):
#     string_in = input()
#     for j in range(4):
#         letter = string_in[j]
#         if letter != ".":
#             orig_x, orig_y = original_pos[string_in[j]]
#             in_x, in_y = [j, i]
#             result += abs(orig_x - in_x) + abs(orig_y - in_y)
#
# print(result)


# 0.05s
# result = 0
#
# for i in range(4):
#     string_in = input()
#     for j in range(4):
#         letter = ord(string_in[j])-65
#         if letter != ".":
#             orig_x, orig_y = letter % 4, letter // 4
#             in_x, in_y = [j, i]
#             result += abs(orig_x - in_x) + abs(orig_y - in_y)
#
# print(result)


