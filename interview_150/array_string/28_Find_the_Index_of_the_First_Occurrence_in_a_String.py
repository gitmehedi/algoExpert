"""
Problems: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

haystack = "sadbutsad"
needle = "sad"

haystack = "leetcode"
needle = "leeto"


def strStr(haystack, needle):
    nlen = len(needle)
    haylen = len(haystack)
    res = []
    for val in range(haylen):
        if haystack[val:val + nlen] == needle:
            res.append(val)

    return 0 if len(res) > 0 else -1


print(strStr(haystack, needle))
