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

"""
Reverse a Array
"""
array = [1, 2, 3, 4, 5, 6, 7]


def reverseArray(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array


print(reverseArray(array))

"""
Reverse a Array with K steps
"""
array = [1, 2, 3, 4, 5, 6, 7]
k = 3


def reverseArray(array, k):
    def reverse(array, start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
        return array

    str_len = len(array)
    if k > str_len:
        k %= str_len
    reverse(array, 0, str_len - 1)
    reverse(array, 0, k - 1)
    reverse(array, k, str_len - 1)

    return array


print(reverseArray(array, k))
