from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits

            digits[i] = 0   
            
        return [1] + digits


if __name__ == "__main__":
    print(Solution().plusOne([1,2,3]))
    print(Solution().plusOne([4,3,2,1]))
    print(Solution().plusOne([9]))