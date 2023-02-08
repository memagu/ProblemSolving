"""
# O(log(n))

class Solution:
    def minPartitions(self, n: str) -> int:
        component_counts = sorted(map(int, n), reverse=True)

        result = component_counts[-1]
        for i in range(len(component_counts)-1):
            result += component_counts[i] - component_counts[i+1]

        return result
"""


# (O(n))

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


if __name__ == "__main__":
    print(Solution().minPartitions("32"))
    print(Solution().minPartitions("82734"))
    print(Solution().minPartitions("27346209830709182346"))
