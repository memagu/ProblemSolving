from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque((root,))
        depth = 1
        max_level_sum = (root.val, 1)  # (level_sum, depth)

        while queue:
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            if level_sum > max_level_sum[0]:
                max_level_sum = (level_sum, depth)

            depth += 1

        return max_level_sum[1]


if __name__ == "__main__":
    print(Solution().maxLevelSum(TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode())))
