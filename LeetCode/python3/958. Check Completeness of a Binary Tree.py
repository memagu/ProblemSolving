from typing import Dict, List, Optional, Tuple
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque((root,))
        anticipate_node = True

        while queue:
            node = queue.popleft()
            left_child = node.left or None
            right_child = node.right or None

            if left_child:
                if not anticipate_node:
                    return False
                queue.append(left_child)
            else:
                anticipate_node = False

            if right_child:
                if not anticipate_node:
                    return False
                queue.append(right_child)
            else:
                anticipate_node = False

        return True


if __name__ == "__main__":
    tree_1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    tree_2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
    print(Solution().isCompleteTree(tree_1))
    print(Solution().isCompleteTree(tree_2))
