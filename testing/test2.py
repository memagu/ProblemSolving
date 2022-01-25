import time
import random


def new(s):
    result = 0

    for i in range(4):
        string_in = s[i]
        for j in range(4):
            letter = ord(string_in[j]) - 65
            if letter != ".":
                orig_x, orig_y = letter % 4, letter // 4
                in_x, in_y = [j, i]
                result += abs(orig_x - in_x) + abs(orig_y - in_y)

    return result


def old(s):
    original_pos = {'A': [0, 0], 'B': [1, 0], 'C': [2, 0], 'D': [3, 0], 'E': [0, 1], 'F': [1, 1], 'G': [2, 1],
                    'H': [3, 1], 'I': [0, 2], 'J': [1, 2], 'K': [2, 2], 'L': [3, 2], 'M': [0, 3], 'N': [1, 3],
                    'O': [2, 3]}
    result = 0

    for i in range(4):
        string_in = s[i]
        for j in range(4):
            letter = string_in[j]
            if letter != ".":
                orig_x, orig_y = original_pos[string_in[j]]
                in_x, in_y = [j, i]
                result += abs(orig_x - in_x) + abs(orig_y - in_y)

    return result


def generate_grid():
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', '.']
    chars = random.sample(chars, 16)
    result = []
    for i in range(4):
        result.append(chars[i * 4: i * 4 + 4])

    return result


def time_code(func, arg, n):
    total_time = 0
    for i in range(n):
        arg = generate_grid()
        t0 = time.time_ns()
        func(arg)
        t1 = time.time_ns()
        total_time += t1 - t0
    return total_time / n


def time_code_arvid(func, arg, n):
    t0 = time.time_ns()
    for i in range(n):
        func(arg)
    t1 = time.time_ns()
    return (t1 - t0) / n

random.seed()

print(time_code(new, generate_grid(), 1000000))
print(time_code(old, generate_grid(), 1000000))
print()
print(time_code_arvid(new, generate_grid(), 1000000))
print(time_code_arvid(old, generate_grid(), 1000000))
