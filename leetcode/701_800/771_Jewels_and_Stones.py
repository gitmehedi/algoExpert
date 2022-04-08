"""
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".



Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0


Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""
import resource
import time

time_start = time.perf_counter()


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # stone = 0
        # for st in jewels:
        #     stone += stones.count(st)
        # return stone
        return sum(map(stones.count, list(jewels)))


jewels, stones = "aA", "aAAbbbb"
# jewels, stones = "z", "ZZ"

obj = Solution()
result = obj.numJewelsInStones(jewels, stones)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
