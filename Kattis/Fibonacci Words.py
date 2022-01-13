
# n_0 = [0]         |                                                   | 0
# n_1 = [1]         |                                                   | 1
# n_2 = n_1 + n_0   |                                                   | 10
# n_3 = n_2 + n_1   | n_1 + n_0 + n_1                                   | 101
# n_4 = n_3 + n_2   | n_1 + n_0 + n_1 + n_1 + n_0                       | 10110
# n_5 = n_4 + n_3   | n_1 + n_0 + n_1 + n_1 + n_0 + n_1 + n_0 + n_1     | 10110101

# import sys
#
#
# def binary_sequence(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         previous_sequence = [1]
#         current_sequence = [1, 0]
#         for _ in range(n - 2):
#             next_sequence = current_sequence + previous_sequence
#             previous_sequence = current_sequence
#             current_sequence = next_sequence
#         return current_sequence
#
#
# for line in sys.stdin:
#     n = int(line)
#     find_sequence = []
#
#     for char in input():
#         find_sequence += [int(char)]
#
#     #print(find_sequence)
#
#     count = 0
#
#     for index in range(len(binary_sequence(n))):
#         #print(binary_sequence(n)[index:index+ len(find_sequence)])
#
#         if find_sequence == binary_sequence(n)[index:index + len(find_sequence)]:
#             count += 1
#
#     print(count)
#

def Fib(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    return Fib(n-1) + Fib(n-2)

print(Fib(32))

# def bins(n):
#     l = ["0", "1"]
#     for i in range(n):
#         if i >= 2:
#             s = l[1] + l[0]
#             l[0] = l[1]
#             l[1] = s
#
#     if n == 0:
#         return "0"
#     if n == 1:
#         return "1"
#     return l[1] + l[0]
#
# print("1011010110110101101011011010110110101101011011010110101")
# print(bins(3))