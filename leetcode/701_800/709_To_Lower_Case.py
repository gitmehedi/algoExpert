"""
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
"""
import resource
import time

time_start = time.perf_counter()


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


s = "Hello"
# s = "here"
# s = "LOVELY"
obj = Solution()
result = obj.toLowerCase(s)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
