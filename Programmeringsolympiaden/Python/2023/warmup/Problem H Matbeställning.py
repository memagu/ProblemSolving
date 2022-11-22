"""
from collections import Counter


friends, dishes, target_dish_amount = map(int, input().split())
wanted_dishes = tuple(map(lambda x: int(x) - 1, input().split()))  # 0-index
dish_prices = tuple(map(int, input().split()))

wanted_dishes_counter = Counter(wanted_dishes)
ordered = set(wanted_dishes)
available = sorted([(dish, price) for dish, price in enumerate(dish_prices) if dish not in ordered], key=lambda x: x[1], reverse=True)

result = 0

for dish in sorted(wanted_dishes, key=lambda x: dish_prices[x], reverse=True):
    if len(ordered) >= target_dish_amount:
        print(result)
        break

    if wanted_dishes_counter[dish] == 1:
        continue

    if available[-1][1] <= dish_prices[dish]:
        continue

    new_dish, new_price = available.pop()
    wanted_dishes_counter[dish] -= 1
    wanted_dishes_counter[new_dish] += 1
    ordered.add(new_dish)
    result += new_price - dish_prices[dish]

else:
    print(-1)

"""

"""
friends_amount, dish_amount, target_dish_amount = map(int, input().split())
wanted_dishes = tuple(map(lambda x: int(x) - 1, input().split()))  # 0-index
dish_prices = tuple(map(int, input().split()))

print(f"{friends_amount=}, {dish_amount=}, {target_dish_amount=}")
print(f"{wanted_dishes=}")
print(f"{dish_prices=}")

ordered = len(set(wanted_dishes))
total_cost = 0

order = list(map(lambda x: [x, 0, 0], wanted_dishes))
print(order)

for i, dish in enumerate(wanted_dishes):
    order[dish][1] += 1

print(order)

order.sort(key=lambda x: dish_prices[x[0]], reverse=True)

print(order)

for dish, count, extra_cost in order:
    if order >= target_dish_amount:
        print(total_cost)
        break

    if
"""

"""
friends_amount, dish_amount, target_dish_amount = map(int, input().split())
wanted_dishes = tuple(map(lambda x: int(x) - 1, input().split()))  # 0-index
dish_prices = tuple(map(int, input().split()))

# print(f"{friends_amount=}, {dish_amount=}, {target_dish_amount=}")
# print(f"{wanted_dishes=}")
# print(f"{dish_prices=}")

ordered = set(wanted_dishes)
total_cost = 0

menue = sorted([[dish, dish in ordered] for dish, _ in enumerate(dish_prices)], key=lambda x: dish_prices[x[0]])

queue = [[dish, 0] for dish in ordered]
for dish in wanted_dishes:
    queue[dish][1] += 1

for dish, is_ordered in menue:
    if is_ordered:
        queue[dish][1] -= 1

print(queue)
print(menue)

result = 0

for offset, (dish, is_ordered) in enumerate(menue):
    if len(ordered) == target_dish_amount:
        # win
        break

    for j, (queued_dish, amount) in enumerate(queue):
        if not amount:
            continue

        if dish_prices[queued_dish] <= dish_prices[dish]:
            continue

        if menue[queued_dish + offset][1]:
            continue

        queue[j][1] -= 1
        ordered.add(dish)
        menue[queued_dish + offset][1] = True
        # result += dish_prices[q] dish_prices[dish]
"""
from collections import Counter


friends_amount, dish_amount, target_dish_amount = map(int, input().split())
wanted_dishes = tuple(map(lambda x: int(x) - 1, input().split()))  # 0-index
dish_prices = tuple(map(int, input().split()))

# print(f"{friends_amount=}, {dish_amount=}, {target_dish_amount=}")
# print(f"{wanted_dishes=}")
# print(f"{dish_prices=}")

ordered = len(set(wanted_dishes))

wanted_counts = Counter(wanted_dishes)
# [dish, [[startdish, count], [startdish, count]]]
menu = sorted(
    [[dish, [[dish, wanted_counts[dish]] if wanted_counts[dish] else [], []]] for dish, _ in enumerate(dish_prices)],
    key=lambda x: dish_prices[x[0]])

for _ in range(len(menu)):
    if ordered >= target_dish_amount:
        result = 0
        for item in menu:
            if not item[1][0]:
                continue

            result += dish_prices[item[0]] - dish_prices[item[1][0][0]]

        print(result)
        break

    for i in range(len(menu) - 1, -1, -1):
        if ordered >= target_dish_amount:
            break

        if not menu[i][1][0]:
            continue

        if menu[i][1][0][1] != 1:
            menu[i][1][1] = [menu[i][1][0][0], menu[i][1][0][1] - 1]
            menu[i][1][0][1] = 1

        if i + 1 == len(menu):
            menu[i][1][1] = []
            continue

        if not menu[i + 1][1][0] and menu[i][1][1] and dish_prices[menu[i][1][0][0]] < dish_prices[menu[i + 1][0]]:
            menu[i + 1][1][0] = menu[i][1][1]
            menu[i][1][1] = []
            ordered += 1
            continue

        menu[i + 1][1][1] = menu[i][1][1]
        menu[i][1][1] = []
else:
    print(-1)
