from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i == "++X" or "X++":
                x += 1

            if i == "++X" or i == "X++":
                x += 1

            if i in ["++X", "X++"]:
                x += 1

            if (i == "--X") or ("X--"):
                x -= 1
        return x


def print_bool(python_object: object) -> None:
    print(f"{type(python_object)}{' ' * (20 - len(str(type(python_object))))}{python_object}{' ' * (20 - len(str(python_object)))}{bool(python_object)}")


print(f"type{' ' * 16}object{' ' * 14}boolean value")
print("-" * 53)
print_bool("")
print_bool("a")
print_bool(0)
print_bool(1)
print_bool(0.0)
print_bool(0.1)
print_bool(0 + 0j)
print_bool(2 + 1j)
print_bool([])
print_bool([1, 2, 3])
print_bool(())
print_bool((1, 2))
print_bool(range(0))
print_bool(range(1))
print_bool({})
print_bool({"a": 1})
print_bool(set())
print_bool({1, 2})
print_bool(frozenset())
print_bool(frozenset((1, 2)))
print_bool(False)
print_bool(True)
print_bool(b"")
print_bool(b"a")
print_bool(bytearray())
print_bool(bytearray(1))
print_bool(None)
