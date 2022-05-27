c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = map(int, input().replace("-", ""))

print(int(not bool((4*c1 + 3*c2 + 2*c3 + 7*c4 + 6*c5 + 5*c6 + 4*c7 + 3*c8 + 2*c9 + 1*c10) % 11)))
