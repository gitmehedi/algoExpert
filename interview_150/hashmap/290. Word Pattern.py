"""
Problem: https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

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



pattern, s = "abba", "dog cat cat dog"
pattern, s = "abba", "dog cat cat fish"
pattern, s = "aaa", "aa aa aa aa"


def wordPattern(pattern, s):
    match = s.split()
    if len(set(pattern)) != len(set(match)) or len(pattern) != len(match):
        return False
    hmap = {}
    for word in range(len(match)):
        if match[word] not in hmap:
            hmap[match[word]] = pattern[word]
        elif hmap[match[word]] != pattern[word]:
            return False
        else:
            pass
    return True


print(wordPattern(pattern, s))