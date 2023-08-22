"""
Longest Substring Without Duplication
"""

s = "clementisacap"


def longestSubStringWithDuplication(s):
    left, right = 0, 0
    visited = set()
    longest = ''
    while left <= right and right < len(s):
        while left < right and s[right] in visited:
            visited.remove(s[left])
            left += 1
        visited.add(s[right])
        longest = max(longest, s[left:right + 1], key=len)
        right += 1
    return longest


print(longestSubStringWithDuplication(s))