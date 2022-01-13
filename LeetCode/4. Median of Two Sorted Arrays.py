nums = []

l = len(nums1) + len(nums2)

for i in range(l):
    if nums1 == []:
        nums += nums2
        break

    if nums2 == []:
        nums += nums1
        break

    if nums1[0] < nums2[0]:
        nums.append(nums1[0])
        nums1.pop(0)
    else:
        nums.append(nums2[0])
        nums2.pop(0)

if l % 2 == 0:
    print((nums[(l) // 2] + nums[(l-2) // 2]) / 2)
else:
    print(nums[(l-1)//2])
