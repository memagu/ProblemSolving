from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = int(self.build_number(l1)[::-1])
        num_2 = int(self.build_number(l2)[::-1])
        result = str(num_1 + num_2)
        return self.build_linked_list(result[::-1])

    def build_number(self, l: Optional[ListNode]) -> str:
        if l.next == None:
            return str(l.val)
        return str(l.val) + self.build_number(l.next)

    def build_linked_list(self, s_reversed: str) -> Optional[ListNode]:
        ll = ListNode(s_reversed[0], None)
        temp = ll
        for number in s_reversed[1:]:
            temp.next = ListNode(number, None)
            temp = temp.next

        return ll
