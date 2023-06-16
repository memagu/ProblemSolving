from collections import defaultdict

input()
input()
entry_times = list(map(int, input().split()))
exit_times = list(map(int, input().split()))

time_diffs = defaultdict(int)

for exit_time in exit_times:
    for entry_time in entry_times:
        if entry_time > exit_time:
            break

        time_diffs[exit_time - entry_time] += 1


print(0 if not time_diffs else min(time_diffs, key=lambda x: (-time_diffs[x], x)))
