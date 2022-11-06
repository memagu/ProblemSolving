from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def to_list(head):
        if head.next is None:
            return [head.val]

        return [head.val] + ListNode.to_list(head.next)

    def __str__(self):
        return str(ListNode.to_list(self))


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_tail = result
        while list1 and list2:
            if list1.val <= list2.val:
                result_tail.next = list1
                list1 = list1.next
                result_tail = result_tail.next
                continue

            result_tail.next = list2
            list2 = list2.next
            result_tail = result_tail.next

        result_tail.next = list1 or list2

        return result.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(1, ListNode(3))

    print(Solution().mergeTwoLists(l1, l3))
