"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        x = 0
        while x < length / 2:
            s[x], s[length - 1 - x] = s[length - 1 - x], s[x]
            x += 1

        return s


s = ["h", "e", "l", "l", "o"]
s = ["H", "a", "n", "n", "a", "h"]
obj = Solution()
print(obj.reverseString(s))
