# https://open.kattis.com/problems/akcija

# <- [2, 3, 4, 4, 6, 9, 10]
# -> [[10, 3, 2], [4, 6 ,4], [9]] = 38
# /> [[10, 3], [6, 4], [9]] = 32
# df = 6

# <- [3, 3, 2, 2]
# -> [[3, 3, 2], [2]] = 10
# /> [[3, 3], [2]] = 8
# df = 2

prices = sorted([int(input()) for i in range(int(input()))], reverse=True)
for i in range(0, len(prices) - 2, 3):
    prices[i+2] = 0
print(sum(prices))