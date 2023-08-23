"""
Longest Substring Without Duplication
"""

s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"


# s = 'bbbab'


def subsequnces(string):
    res = ['']
    palin = ''
    for char in string:
        curr_res = []
        for sub in res:
            seq = char + sub
            curr_res.append(seq)
            # if seq == seq[::-1]:
            #     palin = max(palin, seq, key=len)
        res = res + curr_res

    return res


# print(subsequnces(s))

def get_all_subsequence(s):
    dplen = len(s)
    dp = [[0] * dplen for _ in range(dplen)]
    for i in range(dplen)[::-1]:
        dp[i][i] = 1
        for j in range(i + 1, dplen):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]


# n = input()

print(get_all_subsequence(s))

"""
Longest Increasing Subsequence
"""

nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [4, 2, 1, 4, 3, 4, 5, 8, 15]


def lengthOfLTS(nums):
    dplen = len(nums)
    dp = [[x] for x in nums]

    for i in range(1, dplen):
        maxi, curr = 0, None
        for j in range(i):
            diff = nums[i] - max(dp[j])
            if 0< diff <= 3 and len(dp[j]) > maxi:
                maxi, curr = len(dp[j]), j
        if curr is not None:
            dp[i].extend(dp[curr])

    return max(dp, key=len)[::-1]


print(lengthOfLTS(nums))


def lengthOfLTS(nums):
    dplen = len(nums)
    dp = [0] * dplen
    dp[0] = 1
    for i in range(1, dplen):
        maxi = 0
        for j in range(0, i):
            if nums[i] > nums[j]:
                maxi = max(maxi, dp[j])
        dp[i] = 1 + maxi
    return max(dp)


def substring(string):
    length = len(string)
    window = length
    res = []
    while window > 0:
        offset = 0
        while window + offset <= length:
            sub = string[offset:window + offset]
            if sub == sub[::-1]:
                res.append(sub)
            offset += 1
        window -= 1

    return res


# print(substring(s))

"""
Reverse a string
"""
string = "AlgoExpert is the best!"


def reverseWordsInString(string):
    arr = string.split(" ")
    left, right = 0, len(arr) - 1
    while left < right and left < (left + right) / 2:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return " ".join(arr)


print(reverseWordsInString(string))

"""
32. Longest Valid Parentheses
"""
s = ")(()))"


def longestValidParentheses(s):
    res = 0
    stack = []
    stack.append(-1)
    for st in range(len(s)):
        if s[st] == '(':
            stack.append(st)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(st)
            res = max(res, st - stack[-1])
    return res


print(longestValidParentheses(s))
