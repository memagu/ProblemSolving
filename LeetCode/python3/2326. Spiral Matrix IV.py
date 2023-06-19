from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        col_directions = (1, 0, -1, 0)
        row_directions = (0, 1, 0, -1)
        row = col = direction_index = 0
        matrix = [[-1] * n for _ in range(m)]

        while head:
            matrix[row][col] = head.val

            next_col = col + col_directions[direction_index]
            next_row = row + row_directions[direction_index]

            if not (0 <= next_col < n and 0 <= next_row < m) or matrix[next_row][next_col] != -1:
                direction_index = (direction_index + 1) % 4

            col += col_directions[direction_index]
            row += row_directions[direction_index]

            head = head.next

        return matrix


if __name__ == "__main__":
    print(Solution().spiralMatrix(3, 5, ListNode(
        3,
        ListNode(
            0,
            ListNode(
                2,
                ListNode(
                    6,
                    ListNode(
                        8,
                        ListNode(
                            1,
                            ListNode(
                                7,
                                ListNode(
                                    9,
                                    ListNode(
                                        4,
                                        ListNode(
                                            2,
                                            ListNode(
                                                5,
                                                ListNode(
                                                    5,
                                                    ListNode(
                                                        0
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )))
    print(Solution().spiralMatrix(1, 4, ListNode(
        0,
        ListNode(
            1,
            ListNode(
                2
            )
        )
    )))
