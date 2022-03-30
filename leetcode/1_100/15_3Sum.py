"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

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
import resource
import time
from typing import List

time_start = time.perf_counter()


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ind = 1
        nums.sort()
        length = len(nums)
        arr = []

        while ind < length - 1:
            left = nums[ind - 1]
            middle = nums[ind]
            right = nums[ind + 1]
            if left != middle and middle != right and left != right and (left + middle + right) == 0:
                arr.append((left, middle, right))
            ind += 1

        return arr


nums = [-1, 0, 1, 2, -1, -4]
# nums = []
# nums = [0]
obj = Solution()
result = obj.threeSum(nums)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
