from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"[{self.val}, {self.next}]"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None

        current = head = ListNode()
        while True:
            if not list2 or (list1 and list1.val <= list2.val):
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next

            if not (list1 or list2):
                break

            current.next = current = ListNode()

        return head


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(1, ListNode(3))

    print(Solution().mergeTwoLists(l1, l3))
