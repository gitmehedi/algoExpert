"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2


Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = {}
        for st in s:
            if st in cnt:
                cnt[st] += 1
            else:
                cnt[st] = 1

        even, odd = 0, 0

        for x in cnt.values():
            if x % 2 == 0:
                even += x
            else:
                even += x - 1
                odd = 1
        return even + odd


s = "abccccdd"
s = "ata"
# s = "bb"
s = "ccc"
obj = Solution()
print(obj.longestPalindrome(s))
