operations = [['*'], ['+'], ['-'], ['//', '/']]

def fourth(n):
    for a in operations:
        for b in operations:
            for c in operations:

                if eval(f"4 {a[0]} 4 {b[0]} 4 {c[0]} 4") == n:
                    return f"4 {a[-1]} 4 {b[-1]} 4 {c[-1]} 4 = {n}"

    return "no solution"

for n in range(int(input())):
    print(fourth(int(input())))
