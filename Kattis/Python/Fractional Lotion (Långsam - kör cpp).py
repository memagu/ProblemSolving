while True:
    try:
        n = list(map(int, input().split("/")))[1]
        n = int(n)
        temp = 0

        for x in range(n + 1, n * 2 + 1):
            numerator = x - n
            denominator = x * n
            if denominator % numerator == 0:
                #print(f"1/{x} + 1/{denominator // numerator} = 1/{n}")
                temp += 1
        print(temp)
    except:
        break


# a   c   ad   bc
# - - - = -- - --
# b   d   bd   bd