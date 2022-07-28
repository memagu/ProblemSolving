# https://open.kattis.com/problems/fluortanten

def sign(num):
    if num < 0:
        return -1
    return 1


def evaluate(arr):
    result = 0
    for i, item in enumerate(arr):
        result += (i + 1) * item

    return result


n = int(input())
children = [int(num) for num in input().split() if num != "0"]

increasing = True
decreasing = True
swivel_index = 0
last_num = children[0]

for i, num in enumerate(children[1:]):
    if sign(num) != sign(last_num):
        swivel_index = i + 1
    if num > last_num:
        decreasing = False
    if num < last_num:
        increasing = False
    if not (increasing or decreasing):
        break
    last_num = num

# print(f"{increasing=}, {decreasing=}, {swivel_index}")

if increasing:
    children.insert(swivel_index, 0)
    # print(children)
    maximum = evaluate(children)

elif decreasing:
    children.insert(0, 0)
    # print(children)
    maximum = evaluate(children)
    for i in range(n - 1):
        temp = children[i]
        children[i] = children[i + 1]
        children[i + 1] = temp
        maximum = max(maximum, evaluate(children))
        # print(children)

else:
    children.insert(0, 0)
    # print(children)
    maximum = evaluate(children)
    for i in range(n - 1):
        temp = children[i]
        children[i] = children[i + 1]
        children[i + 1] = temp
        maximum = max(maximum, evaluate(children))
        # print(children)

print(maximum)
