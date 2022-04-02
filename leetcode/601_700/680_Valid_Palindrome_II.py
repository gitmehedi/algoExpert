"""
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""
import resource
import time

time_start = time.perf_counter()


class Solution:
    def validPalindrome(self, s: str) -> bool:
        for val in range(len(s) // 2):
            if s[val] != s[~val]:
                ssub = s[val:~val + 1 or None]
                return (ssub[1:] == ssub[1:][::-1]) or (ssub[:-1] == ssub[:-1][::-1])
        return True


s = "aba"
s = "abca"
s = "aa"
s = "tebbem"
s = "abc"
obj = Solution()
result = obj.validPalindrome(s)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
