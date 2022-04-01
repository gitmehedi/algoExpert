"""
500. Keyboard Row
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]


Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).
"""
import resource
import time
from typing import List

time_start = time.perf_counter()


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fr = "qwertyuiop"
        sr = "asdfghjkl"
        tr = "zxcvbnm"
        ls = []
        for rec in words:
            val = rec.lower()
            fr_len = list(filter(lambda x: x in fr, val))
            sr_len = list(filter(lambda x: x in sr, val))
            tr_len = list(filter(lambda x: x in tr, val))

            if len(fr_len) == len(val):
                ls.append(rec)
            if len(sr_len) == len(val):
                ls.append(rec)
            if len(tr_len) == len(val):
                ls.append(rec)
        return ls


words = ["Hello", "Alaska", "Dad", "Peace"]
words = ["omk"]
words = ["adsdf", "sfd"]
obj = Solution()
result = obj.findWords(words)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
