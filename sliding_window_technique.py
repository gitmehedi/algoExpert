"""
Sliding Window Technique
"""

arr = [100, 200, 300, 400]
k = 2


def maxSum(arr, k):
    length = len(arr)
    max_value = 0
    for row in range(length - k + 1):
        sum = 0
        for col in range(k):
            sum = sum + arr[row + col]
        max_value = max(max_value, sum)

    return max_value


def slidingWindow(arr, k):
    length = len(arr)
    window = sum(arr[:k])
    max_value = window

    for x in range(length - k):
        window = window - arr[x] + arr[x + k]
        max_value = max(window, max_value)

    return max_value


print(maxSum(arr, k))
print(slidingWindow(arr, k))

"""
Find the longest substring of a given string containing k distinct characters
Ref: https://www.techiedelight.com/find-longest-substring-containing-k-distinct-characters/
"""

"""
If K is fixed then the solution would be
"""

s = 'bangladesh'
k = 3


def findLongestSubstringWithK(s, k):
    length = len(s)
    window = set()
    res = ''

    for i in range(length - k + 1):
        window = s[i:i + k]
        unique = set(s[i:i + k])
        if len(window) == len(unique):
            res = window

    return res


print(findLongestSubstringWithK(s, k))

"""
Find the longest substring of a string containing distinct characters
https://www.techiedelight.com/find-longest-substring-given-string-containing-distinct-characters/
"""

s = 'bangladesh'


def findLongestSubstring(s):
    length = len(s)
    window = set()
    res = ''
    k = length
    while k > 1:
        for i in range(length - k + 1):
            window = s[i:i + k]
            unique = set(s[i:i + k])
            if len(window) == len(unique) and len(res) < len(unique):
                res = window

        k -= 1

    return res


print(findLongestSubstring(s))


"""
Longest Palindrome Substring
"""

s = "abbcdafeegh"


def longestPalindrome(s):
    length = len(s)
    window = []
    res = ''
    k = length

    def isPalindrome(string):
        left, right = 0, len(string)-1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1

        return True

    while k > 1:
        for i in range(length - k):
            window = s[i:i + k]
            if isPalindrome(window) and len(window) > len(res):
                res = window
        k -= 1

    return res


print(longestPalindrome(s))