definitions_var_val = {}

while True:
    try:
        instruction = input().split()
    except EOFError:
        break

    if instruction[0] == "def":
        definitions_var_val[instruction[1]] = int(instruction[2])

        # print(definitions_var_val)
        # print(definitions_val_var)

    if instruction[0] == "clear":
        definitions_var_val = {}

    if instruction[0] == "calc":
        unknown = False
        task = instruction[1:-1]
        task_s = ""
        for operation in task:
            if operation in ["-", "+"]:
                task_s += operation
            else:
                try:
                    task_s += str(definitions_var_val[operation])
                except KeyError:
                    unknown = True

        if unknown:
            result = "unknown"
        else:
            try:
                result = list(definitions_var_val.keys())[list(definitions_var_val.values()).index(eval(task_s))]
            except ValueError:
                result = "unknown"

        print(" ".join(instruction[1:]) + " " + result)