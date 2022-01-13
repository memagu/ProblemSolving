import copy

persons = []
for entry in range(int(input())):
    name, liked, date = input().split()
    liked = int(liked)
    persons.append([name, liked, date])

persons.sort(key=lambda x: x[1], reverse=True)
filtered = copy.deepcopy(persons)

for i in range(len(persons) - 1):
    for person in persons[i + 1:]:
        if persons[i][2] == person[2] and person in filtered:
            filtered.remove(person)

filtered.sort(key=lambda x: x[0])

print(len(filtered))
for person in filtered:
    print(person[0])
