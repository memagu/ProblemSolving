variable_value_pairs = {}

while True:
    try:
        line = input().split()
    except EOFError:
        break

    command = line[0]

    if command == "def":
        variable, value = line[1:]
        if variable in variable_value_pairs:
            del variable_value_pairs[variable_value_pairs[variable]]
        value = int(value)

        variable_value_pairs[variable] = value
        variable_value_pairs[value] = variable
        continue

    if command == "calc":
        if line[1] not in variable_value_pairs:
            print(f"{' '.join(line[1:])} unknown")
            continue

        calculated_value = variable_value_pairs[line[1]]

        unknown_variables = False
        for i in range(2, len(line) - 1, 2):
            operation, variable = line[i:i + 2]
            if variable not in variable_value_pairs:
                unknown_variables = True
                break

            if operation == '+':
                calculated_value += variable_value_pairs[variable]
                continue

            calculated_value -= variable_value_pairs[variable]

        if unknown_variables or calculated_value not in variable_value_pairs:
            print(f"{' '.join(line[1:])} unknown")
            continue

        print(f"{' '.join(line[1:])} {variable_value_pairs[calculated_value]}")
        continue

    variable_value_pairs.clear()
