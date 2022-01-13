
SET = 0

while True:

    name_list = []
    name_list_two = []
    name_list_three = []

    n = int(input())

    if n != 0:

        for x in range(n):
            name_list += [input()]

        name_list_two = name_list[1::2]
        name_list = name_list[::2]

        for element in name_list_two:
            name_list_three.insert(0, element)

        name_list += name_list_three

        SET += 1

        print("SET " + str(SET))

        for name in name_list:
            print(name)

    else:
        break
