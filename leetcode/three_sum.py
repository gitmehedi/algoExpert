"""
Problems:
============================
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and
j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105


"""
import time
from itertools import combinations

start_time = time.time_ns()


class Solution(object):
    def threeSum(self, nums):
        vals = []
        for (i, ival), (j, jval), (k, kval) in combinations(enumerate(nums), 3):
            if (ival + jval + kval == 0) and (i != k) and (j != k) and (i != k):
                val = [ival, jval, kval]
                val.sort()
                if val not in vals:
                    vals.append(val)
        return vals


input = [-1, 0, 1, 2, -1, -4]
three_sum = Solution()
output = three_sum.threeSum(input)
print(output)

print("Script Execution Time: %s " % (time.time_ns() - start_time))
