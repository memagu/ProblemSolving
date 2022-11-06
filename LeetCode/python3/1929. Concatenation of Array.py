def getConcatenation(nums: [int]) -> [int]:
    ans = [*nums]
    for elem in nums:
        ans.append(elem)

    return ans