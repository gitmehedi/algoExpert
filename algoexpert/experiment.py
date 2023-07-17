"""
Direct Recursion Sort
"""
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def productSum(array, depth=1):
    sum = 0
    for i in array:
        if type(i) is list:
            depth += 1
            sum += depth * productSum(i, depth)
            depth -= 1
        else:
            sum += i
    return sum


print(productSum(array, depth=1))

s = "aa"
p = "a"


def isMatch(s, p):
    pass


print(isMatch(s, p))

n = 16


def isPowerOfThree(n):
    if n < 0:
        return False

    i = 1
    while i < n:
        i *= 4
    return i == n


print(isPowerOfThree(n))
