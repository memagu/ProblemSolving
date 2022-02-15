len_ltr, len_rtl = map(int, input().split())
ltr, rtl = input(), input()
shift = min(int(input()), len_ltr + len_rtl)

left = range(len_ltr - 1, -1, -1)
right = range(-shift + len_ltr, -shift + len_rtl + len_ltr)

if len_ltr == 0:
    print(rtl)
    exit()

if len_rtl == 0:
    print(ltr[::-1])
    exit()

for i in range(min(min(left), min(right)), max(max(left), max(right)) + 1):
    if i in left:
        if i in right:
            print(rtl[i + shift - len_ltr], end='')

        print(ltr[i * -1 + len_ltr - 1], end='')
        continue

    print(rtl[i + shift - len_ltr], end='')

# len_ltr, let_rtl = map(int, input().split())
# ltr, rtl, shift = input()[::-1], input(), int(input())
# # ltr = left_to_right
# # rtl = right_to_left
# result_1 = list(ltr)
# result_2 = list(rtl)
#
# if not (len_ltr == 0 or let_rtl == 0):
#     for i in range(shift):
#         result_1.insert(-shift + i, rtl[i])
#         result_2.insert(i, '')
#         result_2.pop(i + 1)
#
# print("".join(result_1) + "".join(result_2))
