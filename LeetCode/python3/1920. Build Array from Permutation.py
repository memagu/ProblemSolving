def buildArray(nums:  [int]) -> [int]:
    ans = [nums[nums[i]] for i in range(len(nums))]
    return ans

print(buildArray([5,0,1,2,3,4]))