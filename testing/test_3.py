def two_sum(nums, target):
    hash_map = {num: i for i, num in enumerate(nums)}

    for i, num in enumerate(nums):
        difference = target - num

        if difference in hash_map:
            return [i, hash_map[difference]]

    return None

# nums = [1, 11, 3, 2, 5, 4]
# nums2 = [3, 3]
# target = 15
# print(two_sum(nums, target))
# print(two_sum(nums2, 6))

