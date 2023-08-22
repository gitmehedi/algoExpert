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

"""
Matrix Search
"""
matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]
target = 44


def searchSortedMatrix(matrix, target):
    for key, row in enumerate(matrix):
        for col in range(len(row)):
            if row[col] == target:
                return [key, col]
    return []


print(searchSortedMatrix(matrix, target))
