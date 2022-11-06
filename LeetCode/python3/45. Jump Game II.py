from typing import List

from collections import deque


class Solution:
    def jump_slow(self, nums: List[int]) -> int:
        target = len(nums) - 1
        jumps = 0
        while target != 0:
            target = [i for i in range(target - 1, -1, -1) if i + nums[i] >= target][-1]
            jumps += 1

        return jumps

    def jump_slow_bfs(self, nums: List[int]) -> int:
        visited = set()
        queue = deque([0])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                current_index = queue.popleft()
                if current_index == len(nums) - 1:
                    return depth

                for child in {current_index + delta for delta in range(1, nums[current_index] + 1) if
                              current_index + delta <= len(nums) - 1 and current_index + delta not in visited}:
                    visited.add(child)
                    queue.append(child)

            depth += 1

    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left = right = 0

        while right < len(nums) - 1:
            left, right = right + 1, max(0, *(i + nums[i] for i in range(left, right + 1)))
            jumps += 1

        return jumps


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
    print(Solution().jump([2, 3, 0, 1, 4]))
    print(Solution().jump([1, 1, 1, 1]))
    print(Solution().jump([]))
