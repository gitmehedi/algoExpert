"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        x = len(s)
        while x > 0:
            i = len(s)
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            x = i - len(s)
        return i == 0


parenthesis = "{[[()]]}"
obj = Solution()
print(obj.isValid(parenthesis))
