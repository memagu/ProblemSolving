parts, days = map(int, input().split())

unique_parts = set()

for day in range(1, days + 1):
    unique_parts.add(input())

    if len(unique_parts) == parts:
        print(day)
        break

else:
    print("paradox avoided")
