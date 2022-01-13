def dig(node: ListNode) -> [int]:
    if node.next is not None:
        print(node)
        s = dig(node.next)
        return [*s, node.val * 2 ** (len(s))]

    return [node.val]


return sum(dig(head))
