"""
412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


Constraints:

1 <= n <= 104

"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for nt in range(1, n + 1):
            # This is the first solution
            if nt % 3 == 0 and nt % 5 == 0:
                answer.append('FizzBuzz')
            elif nt % 3 == 0:
                answer.append('Fizz')
            elif nt % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(nt))

            # this is the second solution
            """
            res = list(map(str, range(1, n + 1)))
            res[2::3] = ["Fizz"] * (n // 3)
            res[4::5] = ["Buzz"] * (n // 5)
            res[14::15] = ["FizzBuzz"] * (n // 15)
            return res
            """

        return answer


n = 3
n = 5
n = 15
obj = Solution()
print(obj.fizzBuzz(n))
