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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        list_len = 1
        tail = head.next
        while tail is not None:
            list_len += 1
            tail = tail.next

        delta = list_len - n

        if not delta:
            return head.next

        tail = head
        for j in range(1, delta):
            tail = tail.next

        tail.next = tail.next.next

        return head


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l2 = ListNode(1)
    l3 = ListNode(1, ListNode(2))
    print(Solution().removeNthFromEnd(l1, 2))
    print(Solution().removeNthFromEnd(l2, 1))
    print(Solution().removeNthFromEnd(l3, 1))
