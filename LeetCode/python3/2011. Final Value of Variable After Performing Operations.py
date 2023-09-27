from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(('+' in operation[1]) * 2 - 1 for operation in operations)



if __name__ == "__main__":
    print(Solution().finalValueAfterOperations(["--X","X++","X++"]))
    print(Solution().finalValueAfterOperations(["++X","++X","X++"]))
    print(Solution().finalValueAfterOperations(["X++","++X","--X","X--"]))