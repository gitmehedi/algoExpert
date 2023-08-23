"""

"""
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums):
    left, right = 0, 1
    while left < right and right < len(nums):
        if nums[left] == nums[right]:
            del nums[left]
        else:
            left += 1
            right += 1
    return nums


print(removeDuplicates(nums))
