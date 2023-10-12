from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"[{self.val}, {self.next}]"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                current.next, list1 = list1, list1.next
            else:
                current.next, list2 = list2, list2.next

            current = current.next

        current.next = None or list1 or list2

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(1, ListNode(3))

    print(Solution().mergeTwoLists(l1, l2))
