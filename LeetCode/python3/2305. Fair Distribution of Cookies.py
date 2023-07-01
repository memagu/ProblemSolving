from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookie_amount = len(cookies)
        if cookie_amount == k:
            return max(cookies)

        sums = [0] * k

        def dfs(cookieless_children, depth: int = 0) -> float | int:
            if cookie_amount - depth < cookieless_children:
                return float('inf')

            if depth == cookie_amount:
                return max(sums)

            answer = float('inf')
            for child in range(k):
                cookieless_children -= int(sums[child] == 0)
                sums[child] += cookies[depth]

                answer = min(answer, dfs(cookieless_children, depth + 1))

                sums[child] -= cookies[depth]
                cookieless_children += int(sums[child] == 0)

            return answer

        return dfs(k)


if __name__ == "__main__":
    print(Solution().distributeCookies([8, 15, 10, 20, 8], 2))
    print(Solution().distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3))
    print(Solution().distributeCookies([1, 2], 2))
    print(Solution().distributeCookies([76265, 7826, 16834, 63341, 68901, 58882, 50651, 75609], 8))
