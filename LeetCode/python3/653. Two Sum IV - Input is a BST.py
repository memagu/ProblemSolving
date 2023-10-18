from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        queue = [root]

        while queue:
            node = queue.pop()

            if k - node.val in visited:
                return True

            visited.add(node.val)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return False


if __name__ == "__main__":
    print(Solution().findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 9))
    print(Solution().findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 28))
