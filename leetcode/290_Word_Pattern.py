"""
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False

        pattern_str, s_str = '', ''
        pattern_arr, s_arr = [], []

        for pat in pattern:
            if pat in pattern_arr:
                pattern_str += str(pattern_arr.index(pat))
            else:
                pattern_arr.append(pat)
                pattern_str += str(pattern.index(pat))

        for srt in s_list:
            if srt in s_arr:
                s_str += str(s_arr.index(srt))
            else:
                s_arr.append(srt)
                s_str += str(s_list.index(srt))

        return pattern_str == s_str


pattern = "abddd"
s = "dog cat cat dog"

# pattern = "abba"
# s = "dog cat cat fish"

# pattern = "aaaa"
# s = "dog cat cat dog"
obj = Solution()
print(obj.wordPattern(pattern, s))
