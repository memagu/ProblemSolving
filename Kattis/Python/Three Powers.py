powers_of_three = [str(3 ** x) for x in range(0, 64)]

while True:
    n = int(input())
    if n == 0:
        break

    result = []
    for i in range(64):
        if 1 & (n - 1) >> i:
            result.append(powers_of_three[i])

    if not result:
        print("{ }")
        continue

    print(f"{{ {', '.join(result)} }}")
