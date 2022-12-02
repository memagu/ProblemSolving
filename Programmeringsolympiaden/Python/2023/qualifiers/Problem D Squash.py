from typing import Dict, List, Optional, Tuple

n, k = map(int, input().split())
match_results = list(map(lambda x: 1 - (x == 'F') * 2, input()))


def max_of_k_intervals(i: int, intervals_remaining: int, include: bool, match_results: List[int], memo: Optional[Dict[Tuple[int, int, bool], int]] = None) -> int:
    if memo is None:
        memo = {}

    if (i, intervals_remaining, include) in memo:
        return memo[(i, intervals_remaining, include)]

    if i == len(match_results):
        memo[(i, intervals_remaining, include)] = result = 0
        return result

    result = 0

    if include:
        result = max_of_k_intervals(i + 1, intervals_remaining, True, match_results, memo) + match_results[i]

    elif intervals_remaining > 0:
        result = max_of_k_intervals(i + 1, intervals_remaining - 1, True, match_results, memo) + match_results[i]

    memo[(i, intervals_remaining, include)] = result = max(result, max_of_k_intervals(i + 1, intervals_remaining, False, match_results, memo))

    return result
    
    
print(max_of_k_intervals(0, k, False, match_results))



