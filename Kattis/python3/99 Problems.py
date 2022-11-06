num = input()
if num.endswith("99"):
    print(num)
    quit()

num = int(num)

for i in range(100):
    closest_up = i
    if str(num + i).endswith("99"):
        break

for i in range(100):
    closest_down = i
    if str(num - i).endswith("99"):
        break

add = closest_up if closest_up <= closest_down else -closest_down
print(num + add)


