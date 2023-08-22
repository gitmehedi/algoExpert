"""
Reverse a Interger
"""

x = -123234562


def reverse(x):
    res = 0
    sign = -1 if x < 0 else 1
    x *= sign
    while x > 0:
        res = (res * 10) + (x % 10)
        x //= 10

    result = res * sign

    if result < -2 ** 31 or result > 2 ** 31 - 1:
        return 0

    return result


print(reverse(x))


"""
Reverse a String
"""
string = "Bangladesh"


def reverseStr(string):
    res = []
    pointer = 0
    while pointer < len(string):
        res.insert(0, string[pointer])
        pointer += 1

    return ''.join(res)


print(reverseStr(string))
