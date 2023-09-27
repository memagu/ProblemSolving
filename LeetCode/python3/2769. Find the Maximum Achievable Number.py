class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


if __name__ == "__main__":
    print(Solution().theMaximumAchievableX(4, 1))
    print(Solution().theMaximumAchievableX(3, 2))
