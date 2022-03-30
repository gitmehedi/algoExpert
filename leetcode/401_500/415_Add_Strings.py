"""
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        left = len(num1)
        right = len(num2)
        rng = left if left > right else right
        sm = ''
        remainder = 0
        for val in range(-1, -rng - 1, -1):
            l = int(num1[val]) if abs(val) <= left else 0
            r = int(num2[val]) if abs(val) <= right else 0
            s = str(l + r + remainder)
            if len(s) == 2:
                sm = s[1] + sm
                remainder = int(s[0])
            else:
                sm = s + sm
                remainder = 0
        if remainder > 0:
            sm = str(remainder) + sm

        return sm


num1, num2 = "11", "123"
# num1, num2 = "456", "77"
num1, num2 = "1", "9"
obj = Solution()
print(obj.addStrings(num1, num2))
