"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = len(a) + 1 if len(a) > len(b) else len(b) + 1
        result = ""
        carry = '0'
        for rec in range(1, sum):
            aa = int(a[-rec]) if len(a) >= rec else 0
            bb = int(b[- rec]) if len(b) >= rec else 0
            add = aa + bb + int(carry)
            carry = str(int(add / 2))
            sum_result = add % 2
            result = str(sum_result) + result
        result = carry + result
        return str(int(result))

a = "0"
b = "0"
obj = Solution()
print(obj.addBinary(a, b))
