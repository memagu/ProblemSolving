# l = len(x)
# d = l % 2
# for i in range((l+d) // 2):
#     if x[i] != [-1-i]:
#         return False
# return True

return str(x) == str(x)[::-1]
