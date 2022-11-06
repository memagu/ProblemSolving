_, queries = map(int, input().split())
base_number = 0
variables = {}

for i in range(queries):
    query = input().split()
    if query[0] == "SET":
        variables[query[1]] = query[2]
    if query[0] == "RESTART":
        variables = {}
        base_number = query[1]
    if query[0] == "PRINT":
        if query[1] in variables:
            print(variables[query[1]])
        else:
            print(base_number)
