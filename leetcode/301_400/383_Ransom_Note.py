"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        st = ''
        for ran in list(ransomNote):
            if ran in mag:
                del mag[mag.index(ran)]
                st += ran
        return ransomNote == st


ransomNote, magazine = "a", "b"
ransomNote, magazine = "aa", "bb"
ransomNote, magazine = "aa", "aab"
obj = Solution()
print(obj.canConstruct(ransomNote, magazine))
