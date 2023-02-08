from typing import Dict, List, Optional, Tuple


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        cache = []
        self.dfs(root, cache)
        return cache[-1]

    def dfs(self, node, cache, depth=0):
        if len(cache) == depth:
            cache.append(0)

        if node.left is None and node.right is None:
            cache[depth] += node.val
            return

        if node.left:
            self.dfs(node.left, cache, depth + 1)

        if node.right:
            self.dfs(node.right, cache, depth + 1)
