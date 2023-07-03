from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class DoublyLinkedList:
    value: str = ''
    next: Optional[DoublyLinkedList] = None
    prev: Optional[DoublyLinkedList] = None


root = node = DoublyLinkedList()

for token in input():
    if token == 'L':
        if node.prev is None:
            node.prev = DoublyLinkedList(next=node)
        node = node.prev
        if node.prev is None:
            root = node
        continue

    if token == 'R':
        node = node.next
        continue

    if token == 'B':
        if node.prev is None:
            node.value = ''
            continue

        node = node.prev
        if node.prev is None:
            root = node

        node.next = node.next.next

        if node.next is not None:
            node.next.prev = node

        continue

    if node.value == '':
        node.value = token
        continue

    new_node = DoublyLinkedList(token, node.next, node)
    if new_node.next is not None:
        new_node.next.prev = new_node
    node.next = new_node
    node = new_node

while root:
    print(root.value, end='')
    root = root.next
