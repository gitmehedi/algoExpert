"""
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false


Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
"""
import resource
import time

time_start = time.perf_counter()


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        x = 0
        gl = s
        while x < len(goal):
            gl = gl[1:] + gl[0]
            if goal == gl:
                return True
            x += 1
        return False


s, goal = "abcde", "cdeab"
s, goal = "abcde", "abced"
obj = Solution()
result = obj.rotateString(s, goal)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
