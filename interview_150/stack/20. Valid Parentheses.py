"""
Problem: https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


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
        d = {'(':')', '{':'}','[':']'}
        stack = []

        for val in s:
            if val in d:
                stack.append(val)
            elif len(stack) ==0 or d[stack.pop()] !=val:
                return False
        return len(stack) ==0