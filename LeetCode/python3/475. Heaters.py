from bisect import bisect_left
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        min_radius = 0
        for house in houses:
            closest_right_heater_index = bisect_left(heaters, house)

            left_heater_distance = (
                house - heaters[closest_right_heater_index - 1]
                if closest_right_heater_index > 0 else
                float("inf")
            )

            right_heater_distance = (
                heaters[closest_right_heater_index] - house
                if closest_right_heater_index < len(heaters) else
                float("inf")
            )

            min_radius = max(min_radius, min(left_heater_distance, right_heater_distance))

        return min_radius


if __name__ == "__main__":
    print(Solution().findRadius([1, 2, 3], [2]))
    print(Solution().findRadius([1, 2, 3, 4], [1, 4]))
    print(Solution().findRadius([1, 5], [2]))
    print(Solution().findRadius([1], [1, 2, 3, 4]))
    print(Solution().findRadius([1, 2, 3, 5, 15], [2, 30]))
    print(Solution().findRadius([1, 2, 3, 4, 5, 6], [3, 5]))
