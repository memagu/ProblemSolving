from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"[{self.val}, {self.next}]"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = None

        while head:
            next_node = head.next
            head.next = reversed_list
            reversed_list = head
            head = next_node

        return reversed_list

if __name__ == "__main__":
    print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))  # -> [5, [4, [3, [2, [1, None]]]]]
    print(Solution().reverseList(ListNode(1, ListNode(2))))                                         # ->[2, [1, None]]
    print(Solution().reverseList(None))                                                             # -> None
