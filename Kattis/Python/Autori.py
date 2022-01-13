input = input().split("-")

sNList = []

for name in input:
    sNList.append(name[0])

print(*sNList, sep = "")
