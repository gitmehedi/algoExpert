"""

"""
import resource
import time

time_start = time.perf_counter()


class Solution:
    def functionName(self):
        pass


s = ""
obj = Solution()
result = obj.functionName(s)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
