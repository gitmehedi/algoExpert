"""
Problem: https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150

242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

s, t = "anagram", "nagaram"


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    alno = 26

    freq_s = [0] * alno
    freq_t = [0] * alno

    for i in range(len(s)):
        freq_s[ord(s[i]) - ord('a')] += 1
        freq_t[ord(t[i]) - ord('a')] += 1

    for i in range(alno):
        if freq_s[i] != freq_t[i]:
            return False

    return True


print(isAnagram(s, t))
