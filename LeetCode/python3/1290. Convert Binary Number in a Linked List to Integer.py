class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def dig(node: ListNode) -> [int]:
            if node.next is not None:
                print(node)
                s = dig(node.next)
                return [*s, node.val * 2 ** (len(s))]

            return [node.val]

        return sum(dig(head))
