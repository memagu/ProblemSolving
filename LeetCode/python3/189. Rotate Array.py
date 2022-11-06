def rotate(nums: [int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums.insert(0, nums[-1])
        nums.pop(-1)

    return nums