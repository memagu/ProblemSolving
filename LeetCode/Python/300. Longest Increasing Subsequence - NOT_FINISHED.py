def lengthOfLIS(nums: [int]) -> int:

    cache = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        temp = [0]
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                temp.append(cache[j])

        cache[i] += max(temp)

    return max(cache)




print(lengthOfLIS([11,2,4,12]))