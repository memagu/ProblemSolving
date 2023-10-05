from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    key: int = -1
    value: int = -1
    next: Optional["ListNode"] = None


class MyHashMap:
    def __init__(self):
        self.buckets = [ListNode() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        head = self.buckets[key % len(self.buckets)]

        while head.next is not None:
            if head.next.key == key:
                head.next.value = value
                return

            head = head.next

        head.next = ListNode(key, value)

    def get(self, key: int) -> int:
        head = self.buckets[key % len(self.buckets)]

        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

        return -1

    def remove(self, key: int) -> None:
        bucket_index = key % len(self.buckets)
        head = self.buckets[bucket_index]

        if head is None:
            return

        if head.key == key:
            self.buckets[bucket_index] = head.next
            return

        while head.next is not None:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next


obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
