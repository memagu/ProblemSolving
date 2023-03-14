from typing import Dict, List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        queue = [(root, root.val)]

        while queue:
            node, path_sum = queue.pop()

            if not (node.left or node.right):
                result += path_sum
                continue

            if node.left:
                queue.append((node.left, path_sum * 10 + node.left.val))

            if node.right:
                queue.append((node.right, path_sum * 10 + node.right.val))

        return result


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    tree_2 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    tree_3 = TreeNode(1, TreeNode(5), TreeNode(1, None, TreeNode(6)))

    print(Solution().sumNumbers(tree))
    print(Solution().sumNumbers(tree_2))
    print(Solution().sumNumbers(tree_3))
