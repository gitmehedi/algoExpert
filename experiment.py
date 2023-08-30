"""

"""
# nums = [-1, 0, 1, 2, -1, -4]
nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]


def threeSum(nums):
    nums = sorted(nums)
    result = set()

    for num in range(len(nums)):
        left = num + 1
        right = len(nums) - 1
        while left < right:
            cursum = nums[num] + nums[left] + nums[right]
            if cursum == 0:
                result.add((nums[num], nums[left], nums[right]))
                left += 1
                right -= 1
            elif cursum > 0:
                right -= 1
            elif cursum < 0:
                left += 1

    return result


print(threeSum(nums))
