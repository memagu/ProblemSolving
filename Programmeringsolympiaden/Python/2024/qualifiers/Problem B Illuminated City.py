_, cost, max_average_cost = map(int, (input() for _ in range(3)))
costs = sorted(cost * int(num) for num in input().split())
average_cost = sum(costs) / len(costs)

for i in range(len(costs) - 1, 0, -1):
    if average_cost <= max_average_cost:
        print(i + 1)
        break

    average_cost = (average_cost * (i + 1) - costs[i]) / i
else:
    print(int(average_cost <= max_average_cost))
