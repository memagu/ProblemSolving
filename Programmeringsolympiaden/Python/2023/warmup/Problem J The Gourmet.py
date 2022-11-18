from typing import Dict, Tuple


def get_combinations(time_limit: int, course_times: Tuple[int], time_sum: int = 0, memo: Dict[int, int] = {}) -> int:
    if time_sum not in memo:
        if time_sum > time_limit:
            memo[time_sum] = 0

        elif time_sum == time_limit:
            memo[time_sum] = 1

        else:
            memo[time_sum] = sum(
                get_combinations(time_limit, course_times, time_sum + course_time) for course_time in course_times)

    return memo[time_sum]


time_limit, courses = map(int, (input(), input()))
course_times = tuple(map(int, (input() for _ in range(courses))))

print(get_combinations(time_limit, course_times))
