"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq, non_uniq = [], []
        for st in s:
            if st not in non_uniq:
                uniq.append(st)
                non_uniq.append(st)
            else:
                if st in uniq:
                    uniq.remove(st)

        return s.index(uniq[0]) if len(uniq) > 0 else -1


s = "leetcode"
s = "loveleetcode"
s = "aabb"
s = "aadadaad"
obj = Solution()
print(obj.firstUniqChar(s))
