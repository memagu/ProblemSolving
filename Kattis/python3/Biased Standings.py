for _ in range(int(input())):
    input(), print(sum(abs(i - place) for i, place in enumerate(sorted(int(input().split()[1]) for _ in range(int(input()))), 1)))
