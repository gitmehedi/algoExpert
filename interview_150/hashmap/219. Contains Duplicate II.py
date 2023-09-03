"""
Problem: https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150

219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

nums, k = [1, 2, 3, 1], 3

# nums, k = [1, 0, 1, 1], 1
nums, k = [1, 2, 3, 1, 2, 3], 2


def containsNearbyDuplicate(nums, k):
    res = {}
    for i, val in enumerate(nums):
        if val in res and i - res[val] <= k:
            return True
        res[val] = i
    return False


print(containsNearbyDuplicate(nums, k))
