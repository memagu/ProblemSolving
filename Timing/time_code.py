import time
import generate_args


# multi-timed
def time_code_mt(func, arg, n):
    total_time = 0
    for i in range(n):
        t0 = time.time_ns()
        func(arg)
        t1 = time.time_ns()
        total_time += t1 - t0
    return total_time / n


# single-timed
def time_code_st(func, arg, n):
    t0 = time.time_ns()
    for i in range(n):
        func(arg)
    t1 = time.time_ns()
    return (t1 - t0) / n