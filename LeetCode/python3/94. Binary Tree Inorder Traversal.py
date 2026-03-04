# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class __Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        self.traverse(root, result)

        return result


    def traverse(self, node: TreeNode | None, output: list) -> None:
        if node is None:
            return
        
        self.traverse(node.left, output)
        output.append(node.val)
        self.traverse(node.right, output)


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        stack = [(root, False)]

        while stack:
            node, left_is_visited = stack.pop()

            if node is None:
                continue

            if left_is_visited:
                result.append(node.val)
                stack.append((node.right, False))
            else:
                stack.append((node, True))
                stack.append((node.left, False))

        return result



# if __name__ == "__main__":
#     print(Solution().inorderTraversal([1,None,2,3]))
#     print(Solution().inorderTraversal([1,2,3,4,5,None,8,None,None,6,7,9]))
#     print(Solution().inorderTraversal([]))
#     print(Solution().inorderTraversal([1]))
