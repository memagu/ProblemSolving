from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.__dict__)


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        prev_value = None
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if prev_value is not None:
                min_diff = min(min_diff, node.val - prev_value)
            prev_value = node.val

            node = node.right

        return min_diff



if __name__ == "__main__":
    print(Solution().getMinimumDifference(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))))
    print(Solution().getMinimumDifference(TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))))
