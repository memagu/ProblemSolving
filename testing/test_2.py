from time import perf_counter
start = perf_counter()

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        for o in range(10):
                            for p in range(10):
                                for q in range(10):
                                    for r in range(10):
                                        for s in range(10):
                                            for t in range(10):
                                                print(i, j, k, l, m, n, o, p, q, r, s, t, " | ", perf_counter()-start, sep="")
