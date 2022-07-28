# https://open.kattis.com/problems/fluortanten

def check_order(arr):
    increasing = True
    decreasing = True
    swivel_index = 0

    for i in range(len(arr)-1):
        if not ((arr[i] <= 0 and arr[i+1] <= 0) or (arr[i] >= 0 and arr[i+1] >= 0)):
            swivel_index = i+1
        if arr[i] < arr[i+1]:
            decreasing = False
        if arr[i] > arr[i+1]:
            increasing = False
        if not (increasing or decreasing):
            return None, None

    if increasing:
        return "increasing", swivel_index

    return "decreasing", swivel_index


def evaluate(arr):
    result = 0
    for i, item in enumerate(arr):
        result += (i+1) * item

    return result


n = int(input())
children = [int(num) for num in input().split() if num != "0"]

order, swivel_index = check_order(children)

if order:
    if order == "increasing":
        children.insert(swivel_index, 0)
        maximum = evaluate(children)

    else:
        children.insert(0, 0)
        maximum = evaluate(children)

        for i in range(1, swivel_index-1):
            temp = children[i]
            children[i] = children[i - 1]
            children[i - 1] = temp

            maximum = max(maximum, evaluate(children))

    children.remove(0)
    children.append(0)
    maximum = max(maximum, evaluate(children))

else:
    children += [0]

    maximum = evaluate(children)

    for i in range(n-1, 0, -1):
        temp = children[i]
        children[i] = children[i-1]
        children[i-1] = temp

        maximum = max(maximum, evaluate(children))

print(maximum)
