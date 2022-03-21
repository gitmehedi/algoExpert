"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if len(strs) == 0:
            return prefix

        start_word = strs[0]
        for rec in start_word:
            track = [r.startswith(prefix + rec) for r in strs]
            if sum(track) == len(strs):
                prefix += rec
            else:
                break
        return prefix


strs = ["dog", "racecar", "car"]
obj = Solution()
print(obj.longestCommonPrefix(strs))
