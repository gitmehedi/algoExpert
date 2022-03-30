"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"


Constraints:

1 <= columnNumber <= 231 - 1

URL: https://leetcode.com/problems/excel-sheet-column-title/
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alph = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        st = ''
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber-1, len(alph))
            st = alph[remainder] + st

        return st


columnNumber = 98982
obj = Solution()
print(obj.convertToTitle(columnNumber))
