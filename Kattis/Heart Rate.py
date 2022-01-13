for case in range(int(input())):
    b, p = map(float, input().split())

    ans = b / p * 60
    var = 60 / p

    print(round(ans - var, 4), round(ans, 4), round(ans + var, 4))
