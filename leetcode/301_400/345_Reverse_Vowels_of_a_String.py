"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU'
        start = 0
        end = len(s) - 1
        li = list(s)
        while start < end:
            if li[start] not in vowel:
                start +=1
                continue

            if s[end] not in vowel:
                end -= 1
                continue

            li[start], li[end] = li[end], li[start]
            start += 1
            end -= 1

        return "".join(li)


s = "hello"
s = "leetcodhgfdsafasdSDSDFkjhuyrdhfgiopoiiukgkhe"
obj = Solution()
print(obj.reverseVowels(s))
