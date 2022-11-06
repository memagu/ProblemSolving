Kattis_R2 = False

while Kattis_R2 == True:

    r1, s = input("Tal och medelvärde: ").split()

    r2 = int(s) * 2 - int(r1)

    print("det andra talet är: " + str(r2))

    if input("Vill du köra igen? ") == "Nej" or "nej" or "n":
        break

r1, s = map(int, input().split())

print(s * 2 - r1)