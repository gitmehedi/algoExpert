"""
551. Student Attendance Record I

You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.



Example 1:

Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
Example 2:

Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.


Constraints:

1 <= s.length <= 1000
s[i] is either 'A', 'L', or 'P'.
"""
import resource
import time

time_start = time.perf_counter()


class Solution:
    def checkRecord(self, s: str) -> bool:
        return 'LLL' not in s and s.count('A') < 2

        # absent = 0
        # latecon = 0
        # record = {'ab': 1, 'late': 1}
        # for val in s:
        #     if val == 'A':
        #         absent += 1
        #         if absent == 2:
        #             record['ab'] = 0
        #         latecon = 0
        #     elif val == 'L':
        #         latecon += 1
        #         if latecon == 3:
        #             record['late'] = 0
        #     else:
        #         latecon = 0
        # return sum(record.values()) == 2


s = "PPALLP"
s = "PPALLL"

obj = Solution()
result = obj.checkRecord(s)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
