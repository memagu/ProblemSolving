for case in range(int(input())):
    k, q = input().split(maxsplit=1)
    qn = [int(x) for x in q.split()]
    print(sum(qn) - int(k) + 1)
