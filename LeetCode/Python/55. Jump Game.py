from typing import List, Dict


class Solution:
    def canJump_n2(self, nums: List[int]) -> bool:
        cache = [False for _ in range(len(nums))]
        for i in range(len(nums)):
            if not i:
                cache[i] = True
                continue

            for j in range(i - 1, -1, -1):
                if j + nums[j] >= i:
                    if not cache[j]:
                        continue

                    cache[i] = True
                    break

        return cache[-1]

    def canJump_recursive(self, nums: List[int]) -> bool:
        return self.canJump_recursor(nums)

    def _canJump(self, nums: List[int], memo: Dict[tuple, bool] = {(): True}) -> bool:
        t_nums = tuple(nums)

        if t_nums not in memo:
            memo[t_nums] = len(nums) == 1 or (
                        nums[0] and any(self.canJump_recursor(nums[i:]) for i in range(1, nums[0] + 1)))
        print(memo)

        return memo[t_nums]

    def canJump(self, nums: List[int]) -> bool:
        """
        target = len(nums) - 1
        pointer = target - 1
        while pointer > -1:
            if pointer + nums[pointer] >= target:
                if pointer == 0:
                    return True

                target -= 1

            pointer -= 1

        return false
        """

        target = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target:
                target = i

        return not target




if __name__ == "__main__":
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
    print(Solution().canJump([2, 0, 0]))
