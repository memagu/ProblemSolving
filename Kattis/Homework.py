problems = input().split(";")
result = []
for i, e in enumerate(problems):
    if "-" in e:
        temp = e.split("-")
        e = [str(i) for i in range(int(temp[0]), int(temp[1]) + 1)]
        result += e
        continue
    result.append(e)

print(len(result))