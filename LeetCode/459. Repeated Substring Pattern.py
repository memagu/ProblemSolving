# l = len(s)
# r = (l + l % 2) // 2
#
# for i in range(r):
#     if l % (i+1) == 0:
#         if s[:i+1] * (l // (i+1)) == s:
#             print(True)
#
# print(False)

ss = (s + s)[1:-1]
return s in ss
