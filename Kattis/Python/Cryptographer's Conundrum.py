
days = 0

for i, letter in enumerate(input().lower()):
    per = "per"

    if letter != per[i % 3]:
        days += 1

print(days)
