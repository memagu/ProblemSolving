from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        while True:
            if not list1:
                if list2:
                    while list2.next:
                        result.append(list2.val)
                        list2 = list2.next
                    return self.make_ListNode(result)
                else:
                    return self.make_ListNode(result)

            else:
                if not list2:
                    while list1.next:
                        result.append(list1.val)
                        list1 = list1.next
                    return self.make_ListNode(result)

                if list1.val:
                    if list2.val:
                        if list1.val < list2.val:
                            result.append(list1.val)
                            list1 = list1.next
                        else:
                            result.append(list2.val)
                            list2 = list2.next

    def make_ListNode(self, l):
        current = ListNode(l[0])
        for item in l[1:]:
            current.next = ListNode(item)
            current = current.next
