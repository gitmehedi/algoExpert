"""
Problems: https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150

6. Zigzag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
s = "PAYPALISHIRING"
numRows = 4


def convert(s, numRows):
    if numRows == 1:
        return s
    zigzag = [''] * numRows
    godown = True
    ind = 1
    for ch in s:
        zigzag[ind - 1] += ch

        if ind == numRows:
            godown = False
        elif ind == 1:
            godown = True

        if godown:
            ind += 1
        else:
            ind -= 1
    return ''.join(zigzag)


print(convert(s, numRows))
