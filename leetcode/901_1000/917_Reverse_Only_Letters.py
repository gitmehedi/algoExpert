"""
917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.


Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
"""
import resource
import time

time_start = time.perf_counter()


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_arr = list(s)
        left = 0
        right = len(s)-1

        while left < right:
            if not s_arr[left].isalpha():
                left += 1
            if not s_arr[right].isalpha():
                right -= 1
            if s_arr[left].isalpha() and s_arr[right].isalpha():
                s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                left += 1
                right -= 1

        return ''.join(s_arr)


s = "ab-cd"
s = "a-bC-dEf-ghIj"
# s = "Test1ng-Leet=code-Q!"
obj = Solution()
result = obj.reverseOnlyLetters(s)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
