import heapq
import string


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        """
        6 <= len(password) <= 20

        password.count(lowercase letter) >= 1
        password.count(uppercase letter) >= 1
        password.count(digit) >= 1

        not (password[i] == password[i+1] == password[i+2])
        """
        uppercase = set(string.ascii_uppercase)
        lowercase = set(string.ascii_lowercase)
        digits = set(string.digits)

        required_insertions = max(0, 6 - len(password))
        required_deletions = max(0, len(password) - 20)

        has_upper = any(char in uppercase for char in password)
        has_lower = any(char in lowercase for char in password)
        has_digit = any(char in digits for char in password)

        groups = []
        last_char = password[0]
        count = 0

        for char in password:
            if char == last_char:
                count += 1
            else:
                if count >= 3:
                    groups.append([count % 3, count // 3])
                count = 1
            last_char = char

        if count >= 3:
            groups.append([count % 3, count // 3])

        heapq.heapify(groups)

        for _ in range(required_deletions):
            if not groups:
                break
            rest, triplet_count = heapq.heappop(groups)
            triplet_count -= (not rest)
            rest = (rest - 1) % 3
            if triplet_count:
                heapq.heappush(groups, [rest, triplet_count])

        triplets = sum(triplet_count for _, triplet_count in groups)
        changes = max(triplets, (not has_upper) + (not has_lower) + (not has_digit), required_insertions)

        return changes + required_deletions


if __name__ == "__main__":
    print(Solution().strongPasswordChecker("a"))  # 5
    print(Solution().strongPasswordChecker("aA1"))  # 3
    print(Solution().strongPasswordChecker("1337C0d3"))  # 0
    print(Solution().strongPasswordChecker("aaa111"))  # 2
    print(Solution().strongPasswordChecker("aaaB1"))  # 1
    print(Solution().strongPasswordChecker("ABABABABABABABABABAB1"))  # 2
    print(Solution().strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))  # 8
    print(Solution().strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA"))  # 23
