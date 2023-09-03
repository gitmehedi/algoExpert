"""
Problem: https://leetcode.com/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-interview-150

128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

nums = [100, 1, 3, 2, 200, 4]


def longestConsecutive(nums):
    st = set(nums)
    mx = 0
    for num in nums:
        if num - 1 not in st:
            tmp = 1
            while num + 1 in st:
                tmp += 1
                num += 1
            mx = max(mx, tmp)
    return mx


print(longestConsecutive(nums))
