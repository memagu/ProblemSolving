from typing import Dict, List, Optional, Tuple


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]


if __name__ == "__main__":
    print(Solution().convertTemperature(36.50))
    print(Solution().convertTemperature(122.11))
    print(Solution().convertTemperature(37))
