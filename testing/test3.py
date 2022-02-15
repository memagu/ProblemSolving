def lengthOfLIS(nums: [int]) -> int:

    def lis(nums: [int], d=0):

        if nums:
            sequences = []

            for i, num in enumerate(nums):
                tail = [n for n in nums[i + 1:] if n > num]
                sequences.append(lis(tail, d + 1))
            return max(sequences)

        return d

    print(lis([0, 1, 0, 3, 2, 3]))
    print(lis([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]))


lengthOfLIS([])

# def lengthOfLIS(nums: [int]) -> int:
#     def lis(nums: [int], outer: int, inner: int) -> (int, int, int):  # (tail_outer, tail_inner, tail_alone)
#         if not nums:
#             return 0, 0, 0
#
#         head = nums[0]
#         tail = nums[1:]
#
#         contribution = lis(tail, outer, head)
#         print(contribution)
#         return contribution
#
#         if head > outer:
#             pass
#
#     return max(lis(nums, -10000, -10000))
#
#
# lengthOfLIS([0, 1, 0, 3, 2, 3])

# [0, 1, 0, 3, 2, 3]:-10000,-10000
# [1, 0, 3, 2, 3]: -10000
# [0, 3, 2, 3]
# [3, 2, 3]
# [2, 3]
# [3]
# []
