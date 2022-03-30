"""
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

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

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701


Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        col_sum = 0
        length = len(columnTitle)
        for val in range(length, 0, -1):
            ind = chars.index(columnTitle[val - 1])
            col_sum += (ind + 1) * len(chars) ** (length - val)

        return col_sum


columnTitle = "AAA"
columnTitle = "AB"
columnTitle = "A"

obj = Solution()
print(obj.titleToNumber(columnTitle))
