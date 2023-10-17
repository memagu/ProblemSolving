def generate_state_map(pattern: str) -> tuple[dict[tuple[int, str], int], int]:
    states = {}
    state = 0
    last_instruction = pattern[0]

    for instruction in pattern:
        if instruction == '*':
            states[(state - 1, last_instruction)] = state - 1
            states[(state - 1, '')] = state
            continue

        states[(state, instruction)] = state + 1
        last_instruction = instruction
        state += 1

    return states, state


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        state_map, end_state = generate_state_map(p)

        queue = [(0, 0)]
        visited = set()

        while queue:
            state, i = queue.pop()
            visited.add((state, i))

            if i >= len(s) and state == end_state:
                return True

            for symbol in [''] + ([s[i], '.'] if i < len(s) else []):
                key = (state, symbol)
                if key not in state_map:
                    continue

                next_check = (state_map[key], i + 1 * bool(symbol))
                if next_check in visited:
                    continue
                queue.append(next_check)

        return False


if __name__ == "__main__":
    print(Solution().isMatch("aa", "a"))  # -> False
    print(Solution().isMatch("aa", "a*"))  # -> True
    print(Solution().isMatch("ab", ".*"))  # -> True
    print(Solution().isMatch("aaaabbc", "a*.*c"))  # -> True
    print(Solution().isMatch("aaaabbc", "a*.*d"))  # -> False
    print(Solution().isMatch("aab", "c*a*b"))  # -> True
    print(Solution().isMatch("ccc", "c*a*b"))  # -> False
    print(Solution().isMatch("ccc", "ca*b"))  # -> False
    print(Solution().isMatch("cb", "ca*b"))  # -> True
    print(Solution().isMatch("caaaaaaaaaaaaaab", "ca*b"))  # -> True
    print(Solution().isMatch("bbb", "c*a*b"))  # -> False
    print(Solution().isMatch("b", "c*a*b"))  # -> True
    print(Solution().isMatch("mississippi", "mis*is*p*."))  # -> False
