"""
Problem: https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150

383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

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

ransomNote, magazine = "a", "b"
ransomNote, magazine = "aab", "baa"


def canConstruct(ransomNote, magazine):
    magArr = list(magazine)
    ran = 0
    while ran < len(ransomNote):
        if ransomNote[ran] in magArr:
            ind = magArr.index(ransomNote[ran])
            magArr[ind] = ''
            ran += 1
        else:
            return False
    return True


print(canConstruct(ransomNote, magazine))
