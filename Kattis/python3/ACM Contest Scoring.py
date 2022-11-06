# https://open.kattis.com/problems/acm

score_data = {}
solved_problems = 0

while True:
    s = input()

    if s == "-1":
        break

    submit_time, problem_id, status = s.split()
    submit_time = int(submit_time)

    if status == "right":
        solved_problems += 1

    if problem_id not in score_data:
        score_data[problem_id] = [submit_time, 0, status]
    else:
        score_data[problem_id][0] = submit_time
        score_data[problem_id][1] += 1
        score_data[problem_id][2] = status

time_sum = 0
for problem in score_data.items():
    if problem[1][2] == "wrong":
        continue

    time_sum += problem[1][0] + 20 * problem[1][1]

print(solved_problems, time_sum)